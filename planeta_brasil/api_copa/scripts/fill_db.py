# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import (News, Photo, CulturalProgramming)
from django.core.files import File
from datetime import datetime
import urllib

def run():
    # CREATE AN PHOTO FOR TESTS
    image_url = u'http://www.copa2014.gov.br/sites/default/files/styles/galeria_de_imagem_600_400/public/galeria/img_0592_15d00.jpg'
    img = urllib.urlretrieve(image_url)[0]
    img = File(open(img))

    PHOTO_FILL = Photo.objects.create(photo=img)

    home = {
        "news": [
            {
                'day': '16/04',
                'id': '1',
                'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
                'img': 'images/banner.png'
            },
            {
                'day': '16/04',
                'id': '1',
                'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
                'img': 'images/banner.png'
            },
            {
                'day': '16/04',
                'id': '1',
                'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
                'img': 'images/banner.png'
            },
            {
                'day': '16/04',
                'id': '1',
                'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
                'img': 'images/banner.png'
            },
            {
                'day': '16/04',
                'id': '1',
                'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
                'img': 'images/banner.png'
            }
        ],
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
        "nextMatches": [
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "local": "Maracanã",
                "date": "Quarta 04/06",
                "type": "Amistoso"
            },
        ],
        "lastGames": [
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "gols_home": 2,
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "gols_visited": 1,
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "date": "Quarta 04/06"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "gols_home": 2,
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "gols_visited": 1,
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "date": "Quarta 04/06"
            },
            {
                "home": "Brasil",
                "abbr_home": "BRA",
                "gols_home": 2,
                "img_home": "images/bandeiras/a1.png",
                "visited": "Croacia",
                "gols_visited": 1,
                "abbr_visited": "CRO",
                "img_visited": "images/bandeiras/a2.png",
                "date": "Quarta 04/06"
            },
        ]
        }

    # CREATE NEWS

    def create_new():
        news = home.get('news')

        for new in news:
            day = new.get('day', '')
            day = datetime.strptime(day, '%d/%m').replace(year=2014)

            News.objects.create(
                created=day,
                name_pt=new.get('title', ''),
                name_en=new.get('title', ''),
                name_es=new.get('title', ''),
                photo=PHOTO_FILL,
            )

    # CREATE CulturalProgramming

    def create_cultural_programming():
        cultural_programmings = home.get('culturalProgramming')

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

    create_new()
    create_cultural_programming()
