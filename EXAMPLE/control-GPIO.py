#!/usr/bin/env python
import os
import sys

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

class GIPO:
	def __init__(self):
		if not os.getegid() == 0:
			sys.exit('Script must be run as root')
		self.led=port.PG7
		self.portA=port.PA6
		self.portB=port.PA1
		self.portC=port.PA0
		self.portD=port.PA3
		
		self.dport={self.led:"LED",self.portA:"PORT A",self.portB:"PORT B",self.portC:"PORT C",self.portD:"PORT D"}
		lport=[self.led,self.portA,self.portB,self.portC,self.portD]
		gpio.init()
		for i in lport:
		 #print 'config PORT ',i
		 gpio.setcfg(i, gpio.OUTPUT)

	def dirPort():
		print dir(port)

			 
	def control(self,p,status,debug=False):
		status=int(status)
		if 	 p=='A': port=self.portA
		elif p=='B': port=self.portB
		elif p=='C': port=self.portC
		elif p=='D': port=self.portD
		elif p=='LED': port=self.led
		try:
			gpio.output(port, status)
			if debug:
				print "PORT %s: %d" %(self.dport[port],status)
		except KeyboardInterrupt:
			print ("Goodbye.")

			
