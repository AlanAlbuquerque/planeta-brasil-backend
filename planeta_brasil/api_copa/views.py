#coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from planeta_brasil.util import JsonResponse
from .models import Device, Guess, UserPhoto, WeAre, GuessMatch, Match
from .util import get_state_for_request
from .services import (fetch_news, fetch_cultural_programming,
                       fetch_last_games, fetch_home, fetch_matches_by_groups)
from .scripts import create_we_are
from django.shortcuts import get_object_or_404
from .strings import translation
from .util import DateMultiLanguage


@csrf_exempt
def register_push_device(request):
    try:
        devices = Device.objects.filter(
            push_key=request.POST.get('reg_id')).all()
        if len(devices) == 0:
            device = Device()
            device.push_key = request.POST.get('reg_id')
            device.os = request.POST.get('device_type')
            device.language = request.POST.get('language')
            device.state = get_state_for_request(request)
            device.save()
    except Exception, e:
        print e
    return JsonResponse({})


def api_news(request):
    city = get_state_for_request(request)
    lang = request.GET.get('lang', 1)
    news = fetch_news(lang=lang, city=city)

    return JsonResponse(news)


def api_cultural_programming(request):
    city = get_state_for_request(request)
    lang = request.GET.get('lang', 1)
    cultural_programming = fetch_cultural_programming(lang=lang, city=city)

    return JsonResponse(cultural_programming)


def api_cultural_programming_detail(request, pk):
    city = get_state_for_request(request)
    lang = request.GET.get('lang', 1)
    cultural_programming = fetch_cultural_programming(lang=lang, city=city,
                                                      pk=pk)

    return JsonResponse(cultural_programming)


def api_news_detail(request, pk):
    lang = request.GET.get('lang', 1)
    news = fetch_news(lang=lang, pk=pk)

    return JsonResponse(news)


@csrf_exempt
def api_photos(request):
    if request.FILES:
        try:
            up = UserPhoto()
            up.photo = request.FILES['recFile']
            up.lang = request.GET.get('lang', 1)
            up.city = get_state_for_request(request)
            up.save()
            # destination = open('chegou.jpeg', 'wb+')
            # f = request.FILES['recFile']
            # for chunk in f.chunks():
            #     destination.write(chunk)
            # destination.close()
        except Exception, e:
            print e

    photos = []
    photos_objs = UserPhoto.objects.order_by('-created')[:11]
    for p in photos_objs:
        photos.append({'name': '', 'img': p.thumb.url})
    return JsonResponse(photos)


def api_matches_by_groups(request):
    lang = request.GET.get('lang', 1)
    matches = fetch_matches_by_groups(lang=lang)
    return JsonResponse(matches)


@csrf_exempt
def api_guesses(request):

    guesses = GuessMatch.objects.all()

    dict_guess = {}

    for guess in guesses:
        if guess.result_home > guess.result_visited:
            team_win = guess.match.team_home
        elif guess.result_home < guess.result_visited:
            team_win = guess.match.result_visited
        else:
            team_win = None
        if team_win:
            qtd_win = int(dict_guess.get('qtd_win', 0))
            dict_guess.update({
                team_win.get_field('name', 'pt'): int(qtd_win + 1)})

    guess = {
        1: [
            {'team': 'Brasil', 'percent': '55%'},
            {'team': 'Espanha', 'percent': '23%'},
            {'team': 'Alemanha', 'percent': '12%', },
            {'team': 'Inglaterra', 'percent': '6%', },
            {'team': 'Argentina', 'percent': '4%', },
        ],
        2: [
            {'team': 'Brazil', 'percent': '55%'},
            {'team': 'Spain', 'percent': '23%'},
            {'team': 'Germany', 'percent': '12%', },
            {'team': 'England', 'percent': '6%', },
            {'team': 'Argentine', 'percent': '4%', },
        ],
        3: [
            {'team': 'Brasil', 'percent': '55%'},
            {'team': 'España', 'percent': '23%'},
            {'team': 'Alemanha', 'percent': '12%', },
            {'team': 'Inglaterra', 'percent': '6%', },
            {'team': 'Argentina', 'percent': '4%', },
        ],
    }
    return JsonResponse(guess)


@csrf_exempt
def api_create_guesses(request, pk):
    lang = request.GET.get('lang', 1)
    strings = translation(lang)

    data = {
        u'messages': {
            u'errors': [],
            u'success': u'',
        },
    }

    errors = data['messages']['errors']

    if request.POST:

        result_visited = request.POST.get('visited')
        result_home = request.POST.get('home')
        email = request.POST.get('email')
        name = request.POST.get('name')
        match = get_object_or_404(Match, pk=pk)

        #FIXME What this line create?
        # Guess.objects.create(country=int(request.POST.get('country', '1')))

        email_has_guess_match = GuessMatch.objects.filter(
            match=match, email=str(email)).exists()

        if email_has_guess_match:
            errors.append(strings['email_has_guess_match'])

        else:
            GuessMatch.objects.create(
                email=email,
                name=name,
                result_home=result_home,
                result_visited=result_visited,
                match=match,
            )
            data['messages']['success'] = strings['guess_match_registered_success']


    return JsonResponse(data)


def api_last_games(request):
    lang = request.GET.get('lang', 1)
    page = request.GET.get('page', 0)
    LIMIT = request.GET.get('limit', 10)
    lastGames = fetch_last_games(lang=lang, page=page, limit=LIMIT)

    return JsonResponse(lastGames)


def api_finals(request):
    # lang = request.GET.get('lang', 1)

    def create_match_list(type_match, lang):
        dt = DateMultiLanguage(lang=lang)
        _dict = []
        matches_oitavas = Match.objects.filter(type_match=type_match)\
            .select_relaed('stadium', 'team').order_by('day_match')

        for match in matches_oitavas:
            home = match.team_home
            visited = match.team_visited

            _dict.append({
                "home": home.get_field('name', lang),
                "abbr_home": home.abbr,
                "gols_home": match.result_home,
                "img_home": home.img_app,
                "visited": visited.get_field('name', lang),
                "gols_visited": match.result_visited,
                "abbr_visited": visited.abbr,
                "img_visited": visited.img_app,
                "date": dt.day_week_with_date(match.day_match),
                "local": "%s - %s" % (match.stadium.name,
                                      match.stadium.get_city_display())
            })
        return _dict

    finals = {
        1: {
            'oitavas': create_match_list(3, 1),
            'quartas': create_match_list(4, 1),
            'semi': create_match_list(5, 1),
            'final': create_match_list(7, 1)
            },
        2: {
            'oitavas': create_match_list(3, 2),
            'quartas': create_match_list(4, 2),
            'semi': create_match_list(5, 2),
            'final': create_match_list(7, 2)
            },
        3: {
            'oitavas': create_match_list(3, 3),
            'quartas': create_match_list(4, 3),
            'semi': create_match_list(5, 3),
            'final': create_match_list(7, 3)
            },
    }
    return JsonResponse(finals)


def api_home(request):
    city = get_state_for_request(request)
    lang = request.GET.get('lang', 1)
    home = fetch_home(lang=lang, city=city)

    return JsonResponse(home)


def api_venue_detail(request, pk):
    venue = {
        'id': 1,
        'img': 'images/media/thumb-1.png',
        'title_img': 'Imagem',
        'date': '14/05',
        'title': 'API - OUÇA A MÚSICA OFICIAL DA COPA DO MUNDO NO BRASIL 2014.',
        'message': '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo, alias omnis nisi non! Animi, alias, quidem, odit labore tenetur asperiores quia repudiandae excepturi fugit itaque praesentium accusantium fugiat reiciendis recusandae?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, ducimus, hic, corporis, eveniet fugiat voluptatem vero dignissimos accusantium minus ratione cum officiis ipsum qui rerum aliquid quo repudiandae autem recusandae.</p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, pariatur consequatur doloremque debitis error omnis unde dolorem corporis cum mollitia ducimus voluptates illum repellat delectus enim in soluta nisi natus.</p>',
    }
    return JsonResponse(venue)


def api_we_are(request):
    lang = request.GET.get('lang', 1)

    try:
        obj = WeAre.objects.latest('id')
    except Exception:
        obj = create_we_are.run()

    we_are = {
        "title": obj.get_field('name', lang),
        "description": obj.get_field('description', lang)
    }

    return JsonResponse(we_are)
