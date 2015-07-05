import os

def isIntialNotSet():
	return os.stat("foo.txt").st_size == 0

def setInitialValue(value):
	fo = open("foo.txt", "w")
	print value
	print 'heellel'
	fo.write(str(value));
	fo.close()

def getInitialValue():
	fo = open("foo.txt","r")	
	content = float(fo.read(8));
	print "this is form file file.py"
	print "Initial value is" 
	print content
	fo.close()
	return content

def setEmpty():
	open("foo.txt", 'w').close()
