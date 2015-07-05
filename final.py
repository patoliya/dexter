#import parse
import serverflag
import time
import initialvalue

# import Distance as sensor
from random import randint

def getRandom() :
	return randint(0,15)
	

data = 'false'

while True :
	data = serverflag.parseHtml()
	print data
	if data == 'true' :

		distance = getRandom();
		#distance = sensor.getDistance()

		if initialvalue.isIntialNotSet():

			# startValue =  distance
			startValue = 15;
			initialvalue.setInitialValue(distance)
		else:
			startValue = getInitialValue()

		percnt = (distance/startValue)*100

		serverflag.sendData(percnt)
		#serverflag.sendData()
		#parse.sendData(getRandom())
		#serverflag.sendData()

	else :
		time.sleep(1)
		print 'andriodnot true'
	exit(0)





# print sensor.getDistance
