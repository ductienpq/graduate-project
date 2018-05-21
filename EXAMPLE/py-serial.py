import serial
import time
import json
serport = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
s="ON"
r=''

def recv():
  while True:
    while serport.inWaiting() > 0:
        r=serport.readline().strip()
        s=json.loads(r)
	print "RECV:",r
	print "UNPACK",s['h']

def send(s):
	serport.write(s+"\n")

def control():
  if serport.isOpen():
	serport.flushInput()
	serport.flushOutput()
	print "[OK]. Port Open!"
	while 1:
		#recv()
  		s=raw_input("Enter a value: ")
  		send(s)

recv()

