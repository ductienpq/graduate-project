#THAI-IOT : 1/4/2018
import serial
import time
from datetime import datetime
import json
import platform
from firebase import firebase
import requests
from pytz import timezone
from portJSON import *

databaseURL='https://thai-iot.firebaseio.com/'
firebase = firebase.FirebaseApplication(databaseURL, None)
serport=None


portA=[]

def synData2():
  data=''
  url=databaseURL+'/Timer.json'
  d=None
  try:
    d=requests.get(url).json()
  except:
    print "[ERR]. Disconnect"
    connected_to_internet()
  finally:
    for v,k in d.items():
      data=k
      print v
      for v2 in data:
        try:
            portA.
            print v2['Start'],v2['End'],v2['State']
        except:
            pass
      #if (data[u'Port']==DATA_PORTA.Define):
      #    DATA_PORTA.newJSON(data[u'Start'],data[u'End'],data[u'State'],None)

synData2()

