import webapp2

import csv
import urllib2
import json

url = 'http://images.eurogamer.net/2014/Mark/scorez.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)
rows = []
for row in cr:
    rows.append(row)


resp = json.dumps(rows)

class CSV2JSONP(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request.get("callback", default_value="__callback") + "(" + resp + ")")

application = webapp2.WSGIApplication([
    ('/', CSV2JSONP),
], debug=True)
