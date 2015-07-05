from BeautifulSoup import BeautifulSoup
import json

#import urllib2 
import requests

#html = "<HTML><HEAD><TITLE>ThingWorx&#x3a; Thing com.thingworx.things.ConfiguredThing&#x40;7d3aa373 &#x3a; Response From Execution Of abc</TITLE><LINK rel='Stylesheet' href='/Thingworx/css/thingworxapi.css' type='text/css'></LINK><META http-equiv='Content-Type' content='text/html'></META><META http-equiv='cache-control' content='no-cache, no-store'></META><META http-equiv='expires' content='-1'></META><META http-equiv='pragma' content='no-cache, no-store'></META></HEAD><BODY><IMG SRC=\"/Thingworx/images/ThingworxLogo.png\"/><BR/><H1>abc</H1><TABLE><TR><TH>result</TH></TR><TR><TD>true</TD></TR></TABLE></BODY></HTML>"
#BeautifulSoup(html)
#print html

def parseHtml():
	#html = web.urlopen("http://172.16.1.32:3000").read()
	#BeautifulSoup(html)
	#print html
	headers = {'appKey':'18fe31a8-d6d6-4cba-8eea-03b713fd34c4','Content-Type':'application/json'}

	url = 'https://i3liot4.cloudapp.net:8443/Thingworx/Things/Jar/Services/getStart'
	

	r = requests.post(url, headers=headers,verify = False)
	html = r.text
	parsed_html = BeautifulSoup(html)
	return parsed_html.body.table.td.text
  
#print(parseHtml(html))

def sendData(value):
	headers = {'appKey':'18fe31a8-d6d6-4cba-8eea-03b713fd34c4','Content-Type':'application/json'}
	url = 'https://i3liot4.cloudapp.net:8443/Thingworx/Things/Jar/Services/setPercnt'
	data = {'value':value}
	r = requests.post(url,data=json.dumps(data),headers=headers,verify = False)
	print r.text
	#html = r.text
	#parsed_html = BeautifulSoup(html)
	#return parsed_html.body.table.td.text

