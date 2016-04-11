import zmap
from ipwhois import IPWhois
import pprint
import json
ip_keys = zmap.redis_keys()
hash = file("hash.txt",'r')
term = hash.read()
print "Searching for {}".format(term)
for ip in ip_keys:
    x = zmap.ip_get(ip)
    if term in x:
        spacer = "=" * 24
        print spacer
        print ip
        import GIS
        GIS.GIS(ip)
        print x
        print "Found Golden Key!"
        whois = IPWhois(ip)
        results = whois.lookup()
        print "And it belongs too: "
        pprint.pprint(results)
        print spacer
