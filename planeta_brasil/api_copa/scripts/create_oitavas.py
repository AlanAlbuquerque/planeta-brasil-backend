# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Team, Stadium, Match
from datetime import datetime

def get_team(abbr):
    return Team.objects.get(abbr=abbr)

def run():
    _1A = get_team('1º A')
    _1B = get_team('1º B')
    _1C = get_team('1º C')
    _1D = get_team('1º D')
    _1E = get_team('1º E')
    _1F = get_team('1º F')
    _1G = get_team('1º G')
    _1H = get_team('1º H')
    _2A = get_team('2º A')
    _2B = get_team('2º B')
    _2C = get_team('2º C')
    _2D = get_team('2º D')
    _2E = get_team('2º E')
    _2F = get_team('2º F')
    _2G = get_team('2º G')
    _2H = get_team('2º H')

    oitavas = [
        {
            "day": datetime.strptime("28/06/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Mineirão"),
            "home": _1A,
            "visited": _2B,
            "type": 3,
            "group": '',
        },

        {
            "day": datetime.strptime("28/06/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Maracanã"),
            "home": _1C,
            "visited": _2D,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("29/06/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Castelão"),
            "home": _1B,
            "visited": _2A,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("29/06/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Arena Pernambuco"),
            "home": _1D,
            "visited": _2C,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("30/06/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Nacional de Brasília"),
            "home": _1E,
            "visited": _2F,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("30/06/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Beira Rio"),
            "home": _1G,
            "visited": _2H,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("01/07/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Arena de São Paulo"),
            "home": _1F,
            "visited": _2E,
            "type": 3,
            "group": '',
        },


        {
            "day": datetime.strptime("01/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Arena Fonte Nova"),
            "home": _1H,
            "visited": _2G,
            "type": 3,
            "group": '',
        }
    ]

    def create_quarterfinals():
        for m in oitavas:
            Match.objects.create(
                day_match=m.get('day'),
                type_match=m.get('type'),
                team_home=m.get('home'),
                team_visited=m.get('visited'),
                group=m.get('group'),
                stadium=m.get('stadium'),
        )

    create_quarterfinals()
