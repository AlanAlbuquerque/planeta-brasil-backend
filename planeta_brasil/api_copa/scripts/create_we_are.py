# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import WeAre


def run():

    whe_are = {
            'pt': {
                "title": "Quem somos",
                "description": "<p>A Planeta Brasil possui uma completa estrutura de serviços em hotelaria, transporte, eventos, passeios e outros, pensados para o maior evento de 2014.</p>"
            },
            'en': {
                "title": "About Us",
                "description": "<p>Planeta Brasil has a complete set of services in the hospitality, transportation, events and related industries specifically planned for the biggest event of 2014.</p>"
            },
            'es': {
                "title": "¿Quiénes somos?",
                "description": "<p>Planeta Brasil tiene una estructura de servicios integrales en las industrias de hostelería, transporte, eventos, excursiones y otros planejados especificamente</p>"
            }
        }


    # CREATE WE ARE

    whe_are = WeAre.objects.create(
        name_pt=whe_are['pt']['title'],
        name_en=whe_are['en']['title'],
        name_es=whe_are['es']['title'],
        description_pt=whe_are['pt']['description'],
        description_en=whe_are['en']['description'],
        description_es=whe_are['es']['description'],
    )

    return whe_are
