import zmap
import sys
#a = zmap.Zmaplistoutput()
#print "Module Test: \n [{}]".format(a)
#b = zmap.Zmaplistprobes()
#print "Probe Test: \n [{}]".format(b)
#print "Just port test\n"
#zmap.Zmaptcpscan(80)
try:
    hosts = int(sys.argv[1])
    filename = str(sys.argv[2])
except IndexError:
    print "Defaulting to 10"
    pass
    hosts = 10
print "SSH Test of {} Host\n".format(hosts)
zmap.Zmaptcpscan(port=22,ip=0,count=int(hosts),output=filename)
print "SSH Fetch and Fingerprinting Test"
x = zmap.ssl_parser("ssl.json")
print "Redis Data Extraction Test"
z = zmap.redis_parser("ssl.json")
