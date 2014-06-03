# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Locals
from .get_external_img import img


def run():
    # GET AN PHOTO FOR TESTS
    PHOTO_FILL = img()

    # CREATE Locals
    title ='Trilha da Pedra da Gavea'
    for cp in range(0, 5):
        Locals.objects.create(
            name_pt=title,
            name_en=title,
            name_es=title,
            description_pt=title,
            description_en=title,
            description_es=title,
            photo=PHOTO_FILL.photo,
        )
