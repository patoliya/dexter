import json,httplib

def parseCommon(data):
  connection = httplib.HTTPSConnection('api.parse.com', 443)
  connection.connect()
  connection.request('POST', '/1/push', json.dumps({
         "channels": [''],
         "data": data
       }), {
         "X-Parse-Application-Id": "9B6neGd9ycrpOjK3CBBcb87QrzysZWlRAnnTcmnL",
         "X-Parse-REST-API-Key": "lhLZx8L9L5aUgtImcjKwcWJ4Qi4kngDsUinsJvP3",
         "Content-Type": "application/json"
       })
  result = json.loads(connection.getresponse().read())
  print result


def pushNotification(text):
  parseCommon({
    "alert": text,
    "title": 'Dexter'
  })


def sendData(prcnt):
  print prcnt
  parseCommon({
      "action": "dexter.data",
      'data': prcnt
    })

# sendData(200)
# pushNotification('wassup!')