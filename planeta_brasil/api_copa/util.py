#coding: utf-8
import requests

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
		return REGION_CODE_TO_STATE.get(data['region_code'], None)
	except Exception, e:
		return None 


def get_state_for_request(request):
	if 'HTTP_X_FORWARDED_FOR' in request.META:
		ip_adds = request.META['HTTP_X_FORWARDED_FOR'].split(",")
		ip = ip_adds[0]
	else:
		ip = request.META['REMOTE_ADDR']
	return get_ip_state(ip)
