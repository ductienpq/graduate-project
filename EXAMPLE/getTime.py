import time

def get_Time2(type):
	if (type=='t'):
		localtime = time.localtime(time.time())
		return [localtime[3],localtime[4]]
	
	
print get_Time2('t')