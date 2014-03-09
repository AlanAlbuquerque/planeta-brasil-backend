#coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from planeta_brasil.util import JsonResponse
from .models import News


def api_copa_news(request):
	lang = request.GET.get('lang', 'pt').lower()
	city = request.GET.get('city', None)	
	qs = News.objects.all()
	return JsonResponse([n.as_dict(lang) for n in qs])


def api_copa_videos(request):
	return JsonResponse(dict(a=2))


@csrf_exempt
def register_push_device(request):
	print request
	return JsonResponse({})