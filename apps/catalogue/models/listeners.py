# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.conf import settings
from django.db.models.signals import post_save, pre_delete, post_delete
import django.dispatch
from catalogue.models import Tag, BookMedia, Book, Fragment
from catalogue import tasks
from newtagging.models import tags_updated


def _tags_updated_handler(sender, affected_tags, **kwargs):
    # reset tag global counter
    # we want Tag.changed_at updated for API to know the tag was touched
    for tag in affected_tags:
        tasks.touch_tag(tag)

    # if book tags changed, reset book tag counter
    if isinstance(sender, Book) and \
                Tag.objects.filter(pk__in=(tag.pk for tag in affected_tags)).\
                    exclude(category__in=('book', 'theme', 'set')).count():
        sender.reset_tag_counter()
    # if fragment theme changed, reset book theme counter
    elif isinstance(sender, Fragment) and \
                Tag.objects.filter(pk__in=(tag.pk for tag in affected_tags)).\
                    filter(category='theme').count():
        sender.book.reset_theme_counter()
tags_updated.connect(_tags_updated_handler)


def _pre_delete_handler(sender, instance, **kwargs):
    """ refresh Book on BookMedia delete """
    if sender == BookMedia:
        instance.book.save()
pre_delete.connect(_pre_delete_handler)


def _post_save_handler(sender, instance, **kwargs):
    """ refresh all the short_html stuff on BookMedia update """
    if sender == BookMedia:
        instance.book.save()
post_save.connect(_post_save_handler)


if not settings.NO_SEARCH_INDEX:
    @django.dispatch.receiver(post_delete, sender=Book)
    def _remove_book_from_index_handler(sender, instance, **kwargs):
        """ remove the book from search index, when it is deleted."""
        import search
        search.JVM.attachCurrentThread()
        idx = search.Index()
        idx.open(timeout=10000)  # 10 seconds timeout.
        try:
            idx.remove_book(instance)
            idx.index_tags()
        finally:
            idx.close()
