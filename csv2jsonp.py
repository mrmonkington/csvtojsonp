import webapp2

import csv
import urllib2
import httplib
import json
import socket

from google.appengine.api import memcache

import logging

#http://images.eurogamer.net/2014/Mark/scorez.csv

class CSV2JSONP(webapp2.RequestHandler):
    def fetchCSV(self, url):
        try:
            response = urllib2.urlopen(url)
            cr = csv.reader(response)
            rows = []
            for row in cr:
                rows.append(row)
            resp = json.dumps(rows)
            return resp
        except urllib2.HTTPError, e:
            logging.error('HTTPError: ' + str(e.code) + ' for URL "' + url + '"')
            return "[]"
        except urllib2.URLError, e:
            logging.error('URLError: ' + str(e.reason) + ' for URL "' + url + '"')
            return "[]"
        except httplib.HTTPException, e:
            logging.error('Unspecified HTTPException for URL "' + url + '"')
            return "[]"
        except socket.error, e:
            logging.error('Could not connect to domain or something "' + url + '"')
            return "[]"

    def get(self):
        url=self.request.get("url", default_value="")
        if(url != ""):
            key = "url:" + url
            resp = memcache.get(key)
            if(resp is None):
                resp = self.fetchCSV(url)
                memcache.set(key, resp, 3600)
        else:
            resp = ""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request.get("callback", default_value="__callback") + "(" + resp + ");")

application = webapp2.WSGIApplication([
    ('/', CSV2JSONP),
], debug=True)
