# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Stadium


def run():

    stadiums = [
        {
            "name": "Maracanã",
            "district": "Rio de Janeiro",
        },
        {
            "name": "Mineirão",
            "district": "Belo Horizonte",
        },
        {
            "name": "Arena Amazônia",
            "district": "Manaus",
        },
        {
            "name": "Arena da Baixada",
            "district": "Curitiba",
        },
        {
            "name": "Arena de São Paulo",
            "district": "São Paulo",
        },
        {
            "name": "Arena Fonte Nova",
            "district": "Salvador",
        },
        {
            "name": "Arena Pantanal",
            "district": "Cuiabá",
        },
        {
            "name": "Arena Pernambuco",
            "district": "Recife",
        },
        {
            "name": "Beira Rio",
            "district": "Porto Alegre",
        },
        {
            "name": "Castelão",
            "district": "Fortaleza",
        },
        {
            "name": "Arena das Dunas",
            "district": "Natal",
        },
        {
            "name": "Nacional de Brasília",
            "district": "Brasília",
        }
    ]

    # CREATE Stadium

    def create_stadium():
        for st in stadiums:
            Stadium.objects.create(
                name=st.get('name', ''),
                city=st.get('district', ''),
            )

    create_stadium()
