# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Stadium


def run():

    stadiums = [
        {
            "name": "Maracanã",
            "district": "RJ",
        },
        {
            "name": "Mineirão",
            "district": "MG",
        },
        {
            "name": "Arena Amazônia",
            "district": "AM",
        },
        {
            "name": "Arena da Baixada",
            "district": "PR",
        },
        {
            "name": "Arena de São Paulo",
            "district": "SP",
        },
        {
            "name": "Arena Fonte Nova",
            "district": "BA",
        },
        {
            "name": "Arena Pantanal",
            "district": "MT",
        },
        {
            "name": "Arena Pernambuco",
            "district": "PE",
        },
        {
            "name": "Beira Rio",
            "district": "RS",
        },
        {
            "name": "Castelão",
            "district": "CE",
        },
        {
            "name": "Arena das Dunas",
            "district": "RN",
        },
        {
            "name": "Nacional de Brasília",
            "district": "DF",
        }
    ]

    # CREATE Stadium

    def create_stadium():
        dict_not_creted = []
        for st in stadiums:
            stadium = Stadium.objects.filter(city=st.get('district', ''))

            if not stadium:
                Stadium.objects.create(
                    name=st.get('name', ''),
                    city=st.get('district', ''),
                )
            else:
                dict_not_creted.append(stadium[0].name)

        if dict_not_creted:
            print "Estádio já existe e não foi criado: %s" % (dict_not_creted)

    create_stadium()
