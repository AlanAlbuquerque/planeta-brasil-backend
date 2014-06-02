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
    _1V = get_team(TEAM.abbr)
    _2V = get_team(TEAM.abbr)
    _3V = get_team(TEAM.abbr)
    _4V = get_team(TEAM.abbr)
    _5V = get_team(TEAM.abbr)
    _6V = get_team(TEAM.abbr)
    _7V = get_team(TEAM.abbr)
    _8V = get_team(TEAM.abbr)

    quartas = [
        {
            "day": datetime.strptime("04/07/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Maracanã"),
            "home": _5V,
            "visited": _6V,
            "type": 4,
            "group": '',
        },

        {
            "day": datetime.strptime("04/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Castelão"),
            "home": _1V,
            "visited": _2V,
            "type": 4,
            "group": '',
        },
        {
            "day": datetime.strptime("05/07/2014 13:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(
                name__icontains="Nacional de Brasília"),
            "home": _7V,
            "visited": _8V,
            "type": 4,
            "group": '',
        },
        {
            "day": datetime.strptime("05/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Arena Fonte Nova"),
            "home": _3V,
            "visited": _4V,
            "type": 4,
            "group": '',
        },
    ]

    for m in quartas:
        Match.objects.create(
            day_match=m['day'],
            type_match=m['type'],
            team_home=m["home"],
            team_visited=m["visited"],
            group=m['group'],
            stadium=m['stadium'],
        )

    semi = [
        {
            "day": datetime.strptime("08/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Mineirão"),
            "home": _1V,
            "visited": _2V,
            "type": 5,
            "group": '',
        },

        {
            "day": datetime.strptime("09/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(
                name__icontains="Arena de São Paulo"),
            "home": _3V,
            "visited": _4V,
            "type": 5,
            "group": '',
        },
    ]

    _1P = get_team(TEAM.abbr)
    _2P = get_team(TEAM.abbr)

    terceiro = [
        {
            "day": datetime.strptime("12/07/2014 17:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(
                name__icontains="Nacional de Brasília"),
            "home": _1P,
            "visited": _2P,
            "type": 6,
            "group": '',
        },

    ]

    final = [
        {
            "day": datetime.strptime("13/07/2014 16:00", "%d/%m/%Y %H:%M"),
            "stadium": Stadium.objects.get(name__icontains="Maracanã"),
            "home": _1V,
            "visited": _1V,
            "type": 7,
            "group": '',
        },
    ]

    for m in semi:
        Match.objects.create(
            day_match=m['day'],
            type_match=m['type'],
            team_home=m["home"],
            team_visited=m["visited"],
            group=m['group'],
            stadium=m['stadium'],
        )

    for m in terceiro:
        Match.objects.create(
            day_match=m['day'],
            type_match=m['type'],
            team_home=m["home"],
            team_visited=m["visited"],
            group=m['group'],
            stadium=m['stadium'],
        )

    for m in final:
        Match.objects.create(
            day_match=m['day'],
            type_match=m['type'],
            team_home=m["home"],
            team_visited=m["visited"],
            group=m['group'],
            stadium=m['stadium'],
        )
