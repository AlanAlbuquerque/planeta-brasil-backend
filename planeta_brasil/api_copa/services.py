#coding: utf-8
from django.db.models import Q
from planeta_brasil.api_copa.models import News, CulturalProgramming, Match
from .util import DateMultiLanguage
from planeta_brasil.api_copa.constants import GROUP_CHOICES


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


def fetch_last_games(lang='pt', page=0, limit=10):

    OFFSET = page if not page else int(page) * int(limit)

    dt = DateMultiLanguage(lang=lang)

    lastGames = {
        'items': [],
        'offset': OFFSET,
    }

    matches = Match.objects.filter(is_finished=True)\
        .order_by('-created')[OFFSET:limit+OFFSET]

    for match in matches:
        home = match.team_home
        visited = match.team_visited

        lastGames['items'].append({
            "home": home.get_field('name', lang),
            "abbr_home": home.abbr,
            "gols_home": str(match.result_home),
            "img_home": home.img_app,
            "visited": visited.get_field('name', lang),
            "gols_visited": str(match.result_visited),
            "abbr_visited": visited.abbr,
            "img_visited": visited.img_app,
            "date": dt.day_week_with_date(match.day_match)
        })

    lastGames['total'] = str(len(lastGames['items']))

    return lastGames


def fetch_next_games(lang='pt', page=0, limit=10):

    OFFSET = page if not page else int(page) * int(limit)

    dt = DateMultiLanguage(lang=lang)

    nextGames = {
        'items': [],
        'offset': OFFSET,
    }

    matches = Match.objects.filter(is_finished=False)\
        .order_by('-created')[OFFSET:limit+OFFSET]

    for match in matches:
        home = match.team_home
        visited = match.team_visited

        nextGames['items'].append({
            "home": home.get_field('name', lang),
            "abbr_home": home.abbr,
            "img_home": home.img_app,
            "visited": visited.get_field('name', lang),
            "abbr_visited": visited.abbr,
            "img_visited": visited.img_app,
            "local": match.stadium.name,
            "date": dt.day_week_with_date(match.day_match),
            "type": match.get_type_match_display(),
        })

    nextGames['total'] = str(len(nextGames['items']))

    return nextGames


def fetch_home(lang='pt', city=None):

    news = fetch_news(lang=lang, city=city)
    cp = fetch_cultural_programming(lang=lang, city=city)
    last_games = fetch_last_games(lang=lang, limit=3)
    next_games = fetch_next_games(lang=lang, limit=8)

    home = {
        "news": [news],
        "culturalProgramming": [cp],
        "nextMatches": [next_games['items']],
        "lastGames": [last_games['items']]
    }

    return home


def fetch_matches_by_groups(lang='pt'):
    dt = DateMultiLanguage(lang=lang)
    list_groups = [G[0] for G in GROUP_CHOICES]

    matches = {}

    for group in list_groups:
        obj_group = Match.objects.filter(group=group)
        dict_group = []
        for match in obj_group:
            dict_group.append({
                'day': dt.date_short_str(match.day_match),
                'home': match.team_home.get_field('name', lang),
                'visited': match.team_visited.get_field('name', lang),
                'result': '%s x %s' % (match.result_home,
                                       match.result_visited),
            })
        matches.update({group: dict_group})

    return matches
