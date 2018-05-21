#THAI-IOT : 1/4/2018
import serial
from GPIO import *
import time
from datetime import datetime
import json
import platform
from firebase import firebase
import requests
from pytz import timezone
import json

databaseURL='https://iot-control-96b34.firebaseio.com/'
#databaseURL='https://thai-iot.firebaseio.com/'

firebase = firebase.FirebaseApplication(databaseURL, None)
serport=None

#ARDUINO PORT
portSerial="/dev/ttyACM0"
s="ON"
r=''
state=None

#-----DEFINE EACH PORT----------------------
PORTA='A'
PORTB='B'
PORTC='C'
PORTD='D'


#-----NAME EACH PORT------------------------

PORTA_Name="PORT A"
PORTB_Name="PORT B"
PORTC_Name="PORT C"
PORTD_Name="PORT D"

def get_Time():
	localtime = time.localtime(time.time())
	fmt="%s/%s/%s/%s" %(localtime[0],localtime[1],localtime[2],localtime[3])
	return fmt
	
def get_Time2(type):
	if (type=='t'):
		localtime = time.localtime(time.time())
		return [localtime[3],localtime[4]]
	
def checkOS():
  os=platform.system()
  #print os
  if "Linux" in os:
    return 1
  return 0

#Check Network
def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def send2Firebase(path,data,debug=False):
  if debug: print "[SEND]->FIREBASE: %s" %data
  try:
    result = firebase.post(path, data)
  except:
    print "[ERR]"

def recvfromArduino(debug=False):
  r=''
  s={}
  while serport.inWaiting() > 1:
    try:
	  r=serport.readline().strip()
	  s=json.loads(r)
    except Exception,e:
	  print "ERR",e
    finally:
	  p='/sensor/'+get_Time()
	  try:
	    if s[u'h'] and s[u't']:
	      send2Firebase(p,s,True)
	    else:
	      pass
	  except Exception, e:
	    print "ERR",e
	  
def send2Arduino(s,debug=False):
  if debug: print "[SEND]->ARDUINO: %s" %s
  try:
    serport.write(s+"\n")
  except Exception ,e:
    print "[ERR]" ,e
	

def synData2():
  state_PORTA=state_PORTB=state_PORTC=state_PORTD=None
  data=''  
  d=None
  try:
   d = firebase.get('/Timer', None)
  except:
    print "[ERR]. Disconnect"
	
  finally:
    for k,v in d.items():
        if (k==PORTA):
            state_PORTA=process_State(PORTA,PORTA_Name,v,False)
        elif (k==PORTB):
            state_PORTB=process_State(PORTB,PORTB_Name,v,False)
        elif (k==PORTC):
            state_PORTC=process_State(PORTC,PORTC_Name,v,False)
        elif (k==PORTD):
			state_PORTD=process_State(PORTD,PORTD_Name,v,False)
	if(state_PORTA is not None and state_PORTB is not None and state_PORTC is not None and state_PORTD is not None):
		ss='PORT | A:%s | B:%s | C:%s | D:%s' % (state_PORTA,state_PORTB,state_PORTC,state_PORTD)
		print ss
		s='%s%s%s%s' % (state_PORTA,state_PORTB,state_PORTC,state_PORTD)
		send2Arduino(s,debug=False)
		time.sleep(1)
		recvfromArduino(debug=True)	


    
def process_State(portDefine, portName,v,debug=False):
  stateArray=[]
  #print v
  for v2 in v:
    try:
      stateArray.append(checksynTime(v2['Start'],v2['End'],int(v2['State']),portName,debug))
    except:
      pass
  if debug: print portName,stateArray
  if 1 in stateArray:
      return 1
  else :
      return 0


#check synTime from Server
def checksynTime(from_Time,to_Time,_state,portName,debug):
  state=0
  
  #TIME NOW
  flag_Time=False
  h1=h2=m1=m2=None
  try:
      h1    =int(from_Time.split(":")[0])
      m1    =int(from_Time.split(":")[1])
      
      h2    =int(to_Time.split(":")[0])
      m2    =int(to_Time.split(":")[1])
  except:
     pass
    
  #-----------------
  if (h1 > h2) or (h1==h2 and m1 > m2):
    h_tmp=h1
    m_tmp=m1
            
    h1=h2
    m1=m2            
    h2=h_tmp
    m2=m_tmp	
    flag_Time=True

  if flag_Time:
      if debug:
        print "[1][%s] %d : %d <-- %d : %d" %(portName,h1, m1, h2,m2)
  else:
      if debug:
        print "[0][%s] %d : %d --> %d : %d" %(portName,h1, m1, h2,m2)

  
  h,m= get_Time2('t')

  if flag_Time:
    if h > h1 or h < h2 and (h1 != h2):
        state=0
        if debug:
            print "[1][%s][OFF][H > H1| H<H2 ]" %portName
            
    if h < h1 or h > h2 and (h1 != h2):
        state=1          
        if debug:
            print "[1][%s][ON][H < H1| H > H2 ]" %portName
  else:
    if h < h1 or h > h2 and (h1 != h2):
        state=0
        if debug:
            print "[0][%s][OFF][H > H1| H<H2 ]" %portName
            
    if h > h1 and h < h2 and (h1 != h2):
        state=1
        if debug:
            print "[0][%s][ON][H < H1 | H > H2 ]" %portName

  if h==h1:
    if not flag_Time:
        if m>=m1:
            state=1
            if debug:
                print "[0][%s][ON][H1<=H2] H=H1 | M >= M1" %portName
        else:
            state=0
            if debug:
                print "[1][%s][OFF][H1 = H2, M > M1] H=H1 |" %portName            

    else:
        state=1
        if debug:
            print "[1][%s][ON][H1 > H2] H=H1 | M >= M1" %portName
        else:
            state=0
            if debug:
                print "[0][%s][OFF][H1 = H2] H=H1 | M < M1" %portName
            
  if h==h2:
    if m>m2:
        if not flag_Time:
            state=0
            if debug:
                print "[1][%s][OFF][H1>H2 OR H1=H1, M1>M2]| H=H1 | M>M2" %portName
        else:
            state=1
            if debug:
                print "[1][%s][ON][H1>H2] H=H1 | M<=M1" %portName
    else:
        if not flag_Time:
            state=1
            if debug:
                print "[0][%s][ON] H=H2 | M <= M2" %portName        

  if _state==0:
    state=0
  return state

led1=led2=""

if __name__=='__main__':
  debug=False
  serport = serial.Serial(portSerial, 9600, timeout=1)
  if checkOS()==1:
    while 1:
       if connected_to_internet():
      	  print "Network Online!"
      	  while 1:    
            synData2()
            
       else:
      	  print "Network Offline"
          time.sleep(10)

