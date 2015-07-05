#import parse
import serverflag
import time
import initialvalue

# import Distance as sensor
from random import randint

def getRandom() :
	return randint(0,15)
	
startValue = 0.0
data = 'false'
orderflag = 0

while True :
	data = serverflag.parseHtml()
	print data
	if data == 'true' :

		distance = getRandom();
		
		#distance = sensor.getDistance()
		print distance

		if initialvalue.isIntialNotSet():
		#if startValue == 0:
			startValue =  distance
			#startValue = 15.0
			initialvalue.setInitialValue(startValue)

		else:
			startValue = initialvalue.getInitialValue()

		percnt = (distance/startValue)*100
		print percnt

		serverflag.sendData(percnt)

		if percnt < 20:
			if orderflag == 0:
				serverflag.order()
				orderflag = 1
		else:
			orderflag = 0


		#serverflag.sendData()
		#parse.sendData(getRandom())
		#serverflag.sendData()

	else :
		time.sleep(1)
		print 'andriodnot true'
	exit(0)





# print sensor.getDistance
