# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Photo
from urlparse import urlparse
import urllib2
from django.core.files.base import ContentFile


def img():
    '''
        GET OR CREATE AN PHOTO FOR TESTS
    '''

    try:
        PHOTO_FILL = Photo.objects.latest('id')
    except Exception:
        img_url = 'http://colaemmim.com/wp-content/uploads/2013/04/copa-do-\
mundo-brasil-2014.jpg'
        name = urlparse(img_url).path.split('/')[-1]
        content = ContentFile(urllib2.urlopen(img_url).read())
        PHOTO_FILL = Photo.objects.create()
        PHOTO_FILL.photo.save(name, content, save=True)

    return PHOTO_FILL
