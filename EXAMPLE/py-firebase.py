from firebase import firebase
url='https://iot-control-96b34.firebaseio.com/'
firebase = firebase.FirebaseApplication(url, None)
result = firebase.get('/Timer', None)
import time;

def recv():
  for v,k in result.items():
	print v
	try:
	  d=k[1]
	  print d['Start'], d['End'], d['State']
	except:
	  pass


def send2Firebase(path,data,debug=False):
  if debug: print "[SEND] --> FIREBASE: %s" %data
  try:
    result = firebase.post(path, data)
  except:
    print "[ERR]"

	
#GET VN TIME UTC+7
def get_Time():
	localtime = time.localtime(time.time())
	#year=localtime[0]
	#month=localtime[1]
	#day=localtime[2]
	#hour=localtime[3]
	fmt="%s/%s/%s/%s" %(localtime[0],localtime[1],localtime[2],localtime[3])
	return fmt
	

while 1:
  t='/sensor/'+get_Time()
  send2Firebase(t,"x")
  time.sleep(1)
  print '.',