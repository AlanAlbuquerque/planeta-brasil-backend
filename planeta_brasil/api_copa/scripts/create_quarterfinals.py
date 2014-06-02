# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Team, Stadium, Match
from datetime import datetime


# Team for tests
try:
    TEAM = Team.objects.latest('id')
except Exception:
    pass

def get_team(abbr):
    return Team.objects.get(abbr=abbr)

def run():
    _1A = get_team(TEAM.abbr)
    _1B = get_team(TEAM.abbr)
    _1C = get_team(TEAM.abbr)
    _1D = get_team(TEAM.abbr)
    _1E = get_team(TEAM.abbr)
    _1F = get_team(TEAM.abbr)
    _1G = get_team(TEAM.abbr)
    _1H = get_team(TEAM.abbr)
    _2A = get_team(TEAM.abbr)
    _2B = get_team(TEAM.abbr)
    _2C = get_team(TEAM.abbr)
    _2D = get_team(TEAM.abbr)
    _2E = get_team(TEAM.abbr)
    _2F = get_team(TEAM.abbr)
    _2G = get_team(TEAM.abbr)
    _2H = get_team(TEAM.abbr)

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
