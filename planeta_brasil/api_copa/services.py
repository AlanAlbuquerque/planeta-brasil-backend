#coding: utf-8
from django.db.models import Q
from planeta_brasil.api_copa.models import News, CulturalProgramming


def fetch_cultural_programming(lang='pt', city=None, **kwargs):
    '''
        fetch_cultural_programming(lang=lang, city=city, [pk=pk OR id=pk] )
    '''

    pk = kwargs.get('pk', None)
    pk = pk if pk else kwargs.get('id', None)

    dict_cp = []

    if pk:
        cp = CulturalProgramming.objects.get(pk=pk)
        dict_cp = {
            'id': str(cp.id),
            'img': cp.photo.full.url,
            'title_img': cp.photo.thumb.url,
            'date': cp.created.strftime('%d/%m'),
            'title': cp.get_field('name', lang),
            'message': cp.get_field('description', lang),
        }
    else:
        objs = CulturalProgramming.objects.filter(
            Q(city__isnull=True) | Q(city=city)).order_by('-created')[:11]
        for cp in objs:
            dict_cp.append({
                'id': str(cp.id),
                'title': cp.get_field('name', lang),
                'describ': cp.get_field('description', lang),
                'img': cp.photo.thumb.url
            })

    return dict_cp


def fetch_news(lang='pt', city=None, **kwargs):
    '''
        fetch_news(lang=lang, city=city, [pk=pk OR id=pk] )
    '''

    pk = kwargs.get('pk', None)
    pk = pk if pk else kwargs.get('id', None)

    news = []

    if pk:
        new = News.objects.get(pk=pk)
        news = {
            'id': str(new.id),
            'img': new.photo.full.url,
            'title_img': new.photo.thumb.url,
            'date': new.created.strftime('%d/%m'),
            'title': new.get_field('name', lang),
            'message': new.get_field('description', lang),
        }
    else:
        objs = News.objects.filter(
            Q(city__isnull=True) | Q(city=city)).order_by('-created')[:11]
        for new in objs:
            news.append({
                'day': new.created.strftime('%d/%m'),
                'id': str(new.id),
                'title': new.get_field('name', lang),
                'img': new.photo.thumb.url
            })

    return news


home = {
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
