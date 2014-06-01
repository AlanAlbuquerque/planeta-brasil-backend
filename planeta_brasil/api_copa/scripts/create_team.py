# -*- coding: utf-8 -*-

from planeta_brasil.api_copa.models import Team


def run():

    teamPerGroup = [
        {
            1: u'Brasil',
            2: u'Brazil',
            3: u'Brasil',
            'img_app': 'images/bandeiras/a1.png',
            'abbr': 'BRA'
        },
        {
            1: u'Croácia',
            2: u'Croatia',
            3: u'Croacia',
            'img_app': 'images/bandeiras/a2.png',
            'abbr': 'CRO'
        },
        {
            1: u'México',
            2: u'Mexico',
            3: u'Mexico',
            'img_app': 'images/bandeiras/a3.png',
            'abbr': 'MEX'
        },
        {
            1: u'Camarões',
            2: u'Cameroon',
            3: u'Camerún',
            'abbr': 'CAM'
        },
        {
            1: u'Espanha',
            2: u'Spain',
            3: u'España',
            'img_app': 'images/bandeiras/b1.png',
            'abbr': 'ESP'
        },
        {
            1: u'Holanda',
            2: u'Netherlands',
            3: u'Holanda',
            'abbr': 'HOL'
        },
        {
            1: u'Chile',
            2: u'Chile',
            3: u'Chile',
            'img_app': 'images/bandeiras/b3.png',
            'abbr': 'CHI'
        },
        {
            1: u'Austrália',
            2: u'Australia',
            3: u'Australia',
            'img_app': 'images/bandeiras/b4.png',
            'abbr': 'AUS'
        },
        {
            1: u'Colômbia',
            2: u'Colombian',
            3: u'Colombia',
            'img_app': 'images/bandeiras/c1.png',
            'abbr': 'COL'
        },
        {
            1: u'Grécia',
            2: u'Greece',
            3: u'Grecia',
            'img_app': 'images/bandeiras/c2.png',
            'abbr': 'GRE'
        },
        {
            1: u'Costa do Marfim',
            2: u'Ivory Coast',
            3: u'Costa de Marfil',
            'img_app': 'images/bandeiras/c3.png',
            'abbr': 'CMA'
        },
        {
            1: u'Japão',
            2: u'Japan',
            3: u'Japón',
            'img_app': 'images/bandeiras/c4.png',
            'abbr': 'JAP'
        },
        {
            1: u'Uruguai',
            2: u'Uruguay',
            3: u'Uruguay',
            'img_app': 'images/bandeiras/d1.png',
            'abbr': 'URU'
        },
        {
            1: u'Costa Rica',
            2: u'Costa Rica',
            3: u'Costa Rica',
            'img_app': 'images/bandeiras/d2.png',
            'abbr': 'CRI'
        },
        {
            1: u'Inglaterra',
            2: u'England',
            3: u'Inglaterra',
            'img_app': 'images/bandeiras/d3.png',
            'abbr': 'ING'
        },
        {
            1: u'Itália',
            2: u'Italy',
            3: u'Italia',
            'img_app': 'images/bandeiras/d4.png',
            'abbr': 'ITA'
        },
        {
            1: u'Suíça',
            2: u'Switzerland',
            3: u'Suiza',
            'img_app': 'images/bandeiras/e1.png',
            'abbr': 'SUI'
        },
        {
            1: u'Equador',
            2: u'Equator',
            3: u'Ecuador',
            'img_app': 'images/bandeiras/e2.png',
            'abbr': 'EQU'
        },
        {
            1: u'França',
            2: u'France',
            3: u'Francia',
            'img_app': 'images/bandeiras/e3.png',
            'abbr': 'FRA'
        },
        {
            1: u'Honduras',
            2: u'Honduras',
            3: u'Honduras',
            'img_app': 'images/bandeiras/e4.png',
            'abbr': 'HON'
        },
        {
            1: u'Argentina',
            2: u'Argentine',
            3: u'Argentina',
            'img_app': 'images/bandeiras/f1.png',
            'abbr': 'ARG'
        },
        {
            1: u'Bósnia',
            2: u'Bosnian',
            3: u'Bosnio',
            'img_app': 'images/bandeiras/f2.png',
            'abbr': 'BOS'
        },
        {
            1: u'Irã',
            2: u'Iran',
            3: u'Irán',
            'img_app': 'images/bandeiras/f3.png',
            'abbr': 'IRA'
        },
        {
            1: u'Nigéria',
            2: u'Nigeria',
            3: u'Nigeria',
            'img_app': 'images/bandeiras/f4.png',
            'abbr': 'NIG'
        },
        {
            1: u'Alemanha',
            2: u'Germany',
            3: u'Alemania',
            'img_app': 'images/bandeiras/g1.png',
            'abbr': 'ALE'
        },
        {
            1: u'Portugal',
            2: u'Portugal',
            3: u'Portugal',
            'img_app': 'images/bandeiras/g2.png',
            'abbr': 'POR'
        },
        {
            1: u'Gana',
            2: u'Ghana',
            3: u'Ghana',
            'img_app': 'images/bandeiras/g3.png',
            'abbr': 'GAN'
        },
        {
            1: u'EUA',
            2: u'USA',
            3: u'EUA',
            'img_app': 'images/bandeiras/g4.png',
            'abbr': 'EUA'
        },
        {
            1: u'Bélgica',
            2: u'Belgium',
            3: u'Bélgica',
            'img_app': 'images/bandeiras/h1.png',
            'abbr': 'BEL'
        },
        {
            1: u'Argélia',
            2: u'Algeria',
            3: u'Argelia',
            'img_app': 'images/bandeiras/h2.png',
            'abbr': 'AGE'
        },
        {
            1: u'Rússia',
            2: u'Russian',
            3: u'Rusia',
            'img_app': 'images/bandeiras/h3.png',
            'abbr': 'RUS'
        },
        {
            1: u'Coréia do Sul',
            2: u'South Korea',
            3: u'Corea del Sur',
            'img_app': 'images/bandeiras/h4.png',
            'abbr': 'CSU'
        }
    ]

    # CREATE Team

    def create_team():
        for team in teamPerGroup:
            Team.objects.create(
                name_pt=team.get(1, ''),
                name_en=team.get(2, ''),
                name_es=team.get(3, ''),
                img_app=team.get('img_app', ''),
                abbr=team.get('abbr', ''),
            )

    create_team()
