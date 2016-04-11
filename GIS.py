# -*- coding: utf-8 -*-
import geoip2.database as gis
def GIS(ip):
    reader = gis.Reader('GeoLite2-City.mmdb')
    response = reader.city(ip)
    print "Country: [{}]".format(response.country.name)
    print "State: [{}]".format(response.subdivisions.most_specific.name)
    print "City: [{}]".format(response.city.name)

