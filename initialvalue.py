import os

def isIntialNotSet():
	return os.stat("foo.txt").st_size == 0

def setInitialValue(value):
	fo = open("foo.txt", "w")

	fo.write(value);
	fo.close()

def getInitialValue():
	fo = open("foo.txt","r")	
	content = fo.read(8);
	print "this is form file file.py"
	print "Initial value is" 
	print content
	fo.close()
