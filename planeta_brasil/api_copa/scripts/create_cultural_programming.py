# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Photo, CulturalProgramming
from django.core.files import File
import urllib

def run():
    # CREATE AN PHOTO FOR TESTS
    image_url = u'http://www.copa2014.gov.br/sites/default/files/styles/galeria_de_imagem_600_400/public/galeria/img_0592_15d00.jpg'
    img = urllib.urlretrieve(image_url)[0]
    img = File(open(img))

    PHOTO_FILL = Photo.objects.create(photo=img)

    db = {
        "culturalProgramming": [
            {
                "id": 1,
                "title": "OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.",
                "describ": "Som é cantando por Claudia Leitte, Pitbull e Jennifer Lopez.",
                "img": "images/media/thumb-1.png"
            },
            {
                "id": 1,
                "title": "OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.",
                "describ": "Som é cantando por Claudia Leitte, Pitbull e Jennifer Lopez.",
                "img": "images/media/thumb-1.png"
            },
            {
                "id": 1,
                "title": "OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.",
                "describ": "Som é cantando por Claudia Leitte, Pitbull e Jennifer Lopez.",
                "img": "images/media/thumb-1.png"
            },
            {
                "id": 1,
                "title": "OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.",
                "describ": "Som é cantando por Claudia Leitte, Pitbull e Jennifer Lopez.",
                "img": "images/media/thumb-1.png"
            },
            {
                "id": 1,
                "title": "OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.",
                "describ": "Som é cantando por Claudia Leitte, Pitbull e Jennifer Lopez.",
                "img": "images/media/thumb-1.png"
            }
        ],

        }


    # CREATE CulturalProgramming

    def create_cultural_programming():
        cultural_programmings = db.get('culturalProgramming')

        for cp in cultural_programmings:

            CulturalProgramming.objects.create(
                name_pt=cp.get('title'),
                name_en=cp.get('title'),
                name_es=cp.get('title'),
                description_pt=cp.get('describ'),
                description_en=cp.get('describ'),
                description_es=cp.get('describ'),
                photo=PHOTO_FILL,
            )


    create_cultural_programming()
