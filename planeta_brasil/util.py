#coding: utf-8
import json
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, content={}, status=200, content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content),
                                           status=status, content_type=content_type)