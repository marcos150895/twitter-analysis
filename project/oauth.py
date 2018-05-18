from twython import TwythonStreamer
from mongo import *

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        self.insert(data)
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code, data

    def insert(self, data):
        mon= mongo()
        mon.insertPost(data)

stream = MyStreamer("7oNLyfSizGCIY27atxC10bpmj", "g8f46YmsRIR0AxdIVtDvooJBxvr2MA8NwjZdKnuTjnmfGeg7IH",
                     "882363468187303936-5Dz40L9SVlLjBPHHcykw2q3EXUMCIEi",
                      "DN9ynBUMeSBl0Twf034Jijn7eCIntZHsFYIIhJehDZOSV")

stream.statuses.filter(track='bolsonaro2018,bolsonaroPresidente,geraldoAlckimin2018,geraldoPresidente,lula2018,LulaPresidente2018,leviPresidente,levi2018,ciroPresidente,ciro2018,eymal2018,eymalPresidente,collorPresidente,collor2018,marinaPresidente,marina2018,JoaquimBarbosa2018,boulos2018,boulosPresidente,manuelaPresidente,manuela2018,flavio2018,flavioPresidente,rodrigoMaia2018,rodrigoMaiaPresidente,paulo2018,pauloPresidente,joaoPresidente,joao2018')



