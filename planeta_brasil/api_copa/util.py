#coding: utf-8
import requests
from datetime import datetime


REGION_CODE_TO_STATE = {
    '11': 'SP',
    '19': 'SP',
    '21': 'RJ',
    '31': 'MG',
    '41': 'PR',
    '51': 'RS',
    '61': 'DF',
    '62': 'DF',
    '65': 'MT',
    '71': 'BA',
    '81': 'PE',
    '84': 'RN',
    '85': 'CE',
    '92': 'AM',
}


def get_ip_state(ip):
    try:
        data = requests.get('http://freegeoip.net/json/' + ip).json()
        state = REGION_CODE_TO_STATE.get(data['region_code'], None)
        if state is not None:
            return state.upper()
    except Exception, e:
        pass
    return None


def get_state_for_request(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_adds = request.META['HTTP_X_FORWARDED_FOR'].split(",")
        ip = ip_adds[0]
    else:
        ip = request.META['REMOTE_ADDR']

    #return get_ip_state(ip)
    return 'RJ'


class DateMultiLanguage:
    def __init__(self, *args, **kwargs):
        self.lang = kwargs.pop('lang')

        self.PATTERN_DATE = '%m/%d/%Y' if self.lang == 'en' else '%d/%m/%Y'
        self.PATTERN_DATE_SHORT = '%m/%d'

    def day_week(self, date):
        if self.lang == 'en':
            day_long = datetime.strftime(date, '%A')
        else:
            day = datetime.strftime(date, '%w')
            days = {
                'pt': {
                    '0': u'Domingo',
                    '1': u'Segunda',
                    '2': u'Terça',
                    '3': u'Quarta',
                    '4': u'Quinta',
                    '5': u'Sexta',
                    '6': u'Sábado',
                },

                'es': {
                    '0': u'Domingo',
                    '1': u'Lunes',
                    '2': u'Martes',
                    '3': u'Miércoles',
                    '4': u'Jueves',
                    '5': u'Viernes',
                    '6': u'Sábado',
                },
            }
            day_long = days[self.lang][day]

        return day_long

    def date_str(self, date):
        return datetime.strftime(date, self.PATTERN_DATE)

    def day_week_with_date(self, date):
        day_week = self.day_week(date)
        date_short = datetime.strftime(date, self.PATTERN_DATE_SHORT)
        return '%s %s' % (day_week, date_short)
