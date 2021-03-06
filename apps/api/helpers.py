# -*- coding: utf-8 -*-

from time import mktime
from piston.resource import Resource

def timestamp(dtime):
    "converts a datetime.datetime object to a timestamp int"
    return int(mktime(dtime.timetuple()))

class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt"""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)
