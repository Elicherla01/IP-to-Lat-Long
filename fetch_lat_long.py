import ast
import urllib.request
import pandas as pd
def fetch_lat_long(IP_Address):
    #for i in list:
    url = 'http://ip-api.com/json/' + IP_Address
    req = urllib.request.Request(url)
    out = urllib.request.urlopen(req).read()
    #print(out)
    a= out
    k=ast.literal_eval(a.decode('utf-8'))
    #print(k)
    lat = k.get("lat")
    lon = k.get("lon")
    ll=[lat]
    lo=[lon]
    latlong=[ll,lo]
    print(latlong)


fetch_lat_long('203.191.56.3')
