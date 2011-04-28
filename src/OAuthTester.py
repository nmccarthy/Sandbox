oauth = 'oauthtokenhere'
endpoint = '/api/v1/users.json?access_token=' + oauth

import httplib

yamconn = httplib.HTTPSConnection("www.yammer.com")

yamconn.request('GET', endpoint)
raw = yamconn.getresponse()

print(str(raw.status) + ' ' + str(raw.reason))