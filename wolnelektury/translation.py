# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#

from modeltranslation.translator import translator, TranslationOptions
from infopages.models import InfoPage
from catalogue.models import Book

class InfoPageTranslationOptions(TranslationOptions):
    fields = ('page_title', 'title', 'left_column', 'right_column')

translator.register(InfoPage, InfoPageTranslationOptions)

class BookTranslationOptions(TranslationOptions):
    fields = ('_short_html', )

translator.register(Book, BookTranslationOptions)

