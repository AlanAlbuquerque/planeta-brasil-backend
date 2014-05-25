#coding: utf-8
from gcm import GCM

gcm = GCM('AIzaSyCIrW_gpOaY4fmlP-U1Ing3mRvA8Zkvj28')

def send_push():
	reg_ids = ["APA91bH16i4vW5IMOU4IoQCJpvm-1ZChYtI9GnGDBALZ6mktvbl-vcd9OYm8nLBUPzt0Wj_Ou5tbZmfzLQsg4vjO7WZ8KDYTDW7LJ12OkIBpaQ6wre4A5coy-hkdy3QBNtezqJfpZ4Ie7QamMTbMMzN9qbzhFp73b59cvRBJb3SQUmIl1nJQTaE",]
	data = dict(message='teste do python', msgcnt='42', soundname='beep.wav', title='Titulo')
	gcm.json_request(reg_ids, data)