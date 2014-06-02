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
            dict_guess.update({team_win.get_field('name', 'pt'): int(qtd_win + 1)})

    guess = {
        1: [ { 'team': '_Brasil', 'percent': '55%' },
            { 'team': 'Espanha', 'percent': '23%' },
            { 'team': 'Alemanha', 'percent':'12%', },
            { 'team': 'Inglaterra', 'percent':'6%', },
            { 'team': 'Argentina', 'percent':'4%', },
        ],

        2: [ { 'team': '_Brazil', 'percent': '55%' },
            { 'team': 'Spain', 'percent': '23%' },
            { 'team': 'Germany', 'percent':'12%', },
            { 'team': 'England', 'percent':'6%', },
            { 'team': 'Argentine', 'percent':'4%', },
            ],
        3: [ { 'team': '_Brasil', 'percent': '55%' },
             { 'team': 'España', 'percent': '23%' },
            { 'team': 'Alemanha', 'percent':'12%', },
            { 'team': 'Inglaterra', 'percent':'6%', },
            { 'team': 'Argentina', 'percent':'4%', }
            ]
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
    OITAVAS = [
                {
                    "home": "1º grupo A",
                    "abbr_home": "1º A",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo B",
                    "gols_visited": '',
                    "abbr_visited": "2º B",
                    "img_visited": "",
                    "date": "Sábado 28/06",
                    "local": 'Minerão - Belo Horizonte'
                },
                {
                    "home": "1º grupo C",
                    "abbr_home": "1º C",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo D",
                    "gols_visited": '',
                    "abbr_visited": "2º D",
                    "img_visited": "",
                    "date": "Sábado 28/06",
                    "local": "Maracanã - Rio de Janeiro"
                },
                {
                    "home": "1º grupo B",
                    "abbr_home": "1º B",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo A",
                    "gols_visited": '',
                    "abbr_visited": "2º A",
                    "img_visited": "",
                    "date": "Domingo 29/06",
                    "local": "Castelão - Fortaleza"
                },
                {
                    "home": "1º grupo D",
                    "abbr_home": "1º D",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo C",
                    "gols_visited": '',
                    "abbr_visited": "2º C",
                    "img_visited": "",
                    "date": "Domingo 29/06",
                    "local": "Arena Pernanbuco - Recife"
                },
                {
                    "home": "1º grupo E",
                    "abbr_home": "1º E",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo F",
                    "gols_visited": '',
                    "abbr_visited": "2º F",
                    "img_visited": "",
                    "date": "Segunda-feira 30/06",
                    "local": "Nacional de Brasília - Brasília"
                },
                {
                    "home": "1º grupo G",
                    "abbr_home": "1º G",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo H",
                    "gols_visited": '',
                    "abbr_visited": "2º H",
                    "img_visited": "",
                    "date": "Segunda-feira 30/06",
                    "local": "Beira Rio - Porto Alegre"
                },
                {
                    "home": "1º grupo F",
                    "abbr_home": "1º F",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo E",
                    "gols_visited": '',
                    "abbr_visited": "2º E",
                    "img_visited": "",
                    "date": "Terça-feira 01/07",
                    "local": "Arena São Paulo - São Paulo"
                },
                {
                    "home": "1º grupo H",
                    "abbr_home": "1º H",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º grupo G",
                    "gols_visited": '',
                    "abbr_visited": "2º G",
                    "img_visited": "",
                    "date": "Terça-feira 01/07",
                    "local": "Fonte Nova - Salvador"
                }
            ]
    QUARTAS = [
                {
                    "home": "1º classificado",
                    "abbr_home": "1",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "2º classificado",
                    "gols_visited": '',
                    "abbr_visited": "2",
                    "img_visited": "",
                    "date": "Sexta-feira 04/07 ",
                    "local": 'Castelão - Fortaleza'
                },
                {
                    "home": "3º classificado",
                    "abbr_home": "3",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "4º classificado",
                    "gols_visited": '',
                    "abbr_visited": "4",
                    "img_visited": "",
                    "date": "Sexta-feira 04/07 ",
                    "local": "Maracanã - Rio de Janeiro"
                },
                {
                    "home": "5º classificado",
                    "abbr_home": "5",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "6º classificado",
                    "gols_visited": '',
                    "abbr_visited": "6",
                    "img_visited": "",
                    "date": "Sábado 05/07",
                    "local": "Fonte Nova - Salvador"
                },
                {
                    "home": "7º classificado",
                    "abbr_home": "7",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "8º classificado",
                    "gols_visited": '',
                    "abbr_visited": "8",
                    "img_visited": "",
                    "date": "Sábado 05/07",
                    "local": "Nacional de Brasília - Brasília"
                }
            ]
    SEMI = [
            {
                "home": "1º classificado",
                "abbr_home": "1",
                "gols_home": '',
                "img_home": "",
                "visited": "2º classificado",
                "gols_visited": '',
                "abbr_visited": "2",
                "img_visited": "",
                "date": "Terça-feira 08/07",
                "local": 'Minerão - Belo Horizonte'
            },
            {
                "home": "3º classificado",
                "abbr_home": "3",
                "gols_home": '',
                "img_home": "",
                "visited": "4º classificado",
                "gols_visited": '',
                "abbr_visited": "4",
                "img_visited": "",
                "date": "Quarta-feira 09/07 ",
                "local": "Arena São Paulo - São Paulo"
            }
        ]
    FINAL = [
                {
                    "home": "Perdedor 1",
                    "abbr_home": "1",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "Perdedor 2",
                    "gols_visited": '',
                    "abbr_visited": "2",
                    "img_visited": "",
                    "date": "Sábado 12/07",
                    "local": 'Nacional de Brasília - Brasília'
                },
                {
                    "home": "Ganhador 1",
                    "abbr_home": "1",
                    "gols_home": '',
                    "img_home": "",
                    "visited": "Ganhador 2",
                    "gols_visited": '',
                    "abbr_visited": "2",
                    "img_visited": "",
                    "date": "Domingo 13/07",
                    "local": 'Maracanã - Rio de Janeiro'
                }
            ]


    finals = {
        1: {
            'oitavas': OITAVAS,
            'quartas': QUARTAS,
            'semi': SEMI,
            'final': FINAL
            },
        2: {
            'oitavas': OITAVAS,
            'quartas': QUARTAS,
            'semi': SEMI,
            'final': FINAL
            },
        3: {
            'oitavas': OITAVAS,
            'quartas': QUARTAS,
            'semi': SEMI,
            'final': FINAL
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
