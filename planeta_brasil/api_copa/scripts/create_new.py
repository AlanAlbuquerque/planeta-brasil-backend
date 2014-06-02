# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import News
from datetime import datetime
from .get_external_img import img


def run():
    PHOTO_FILL = img()

    db = {
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

        }

    # CREATE NEWS

    def create_news():
        news = db.get('news')

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

    create_news()
