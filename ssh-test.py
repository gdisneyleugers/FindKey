import zmap
import sys
# -*- coding: utf-8 -*-
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
    print "Defaulting to count [10]"
    print "Defaulting to filename [ssh]"
    pass
    hosts = 10
    filename = "ssh"
print "SSH Test of {} Host\n".format(hosts)
try:
    zmap.Zmaptcpscan(port=22,ip=0,count=int(hosts),output=filename)
    print "SSH Fetch and Fingerprinting Test"
except KeyboardInterrupt:
    z = raw_input("Exit Scan [Y/N]: ")
    if "Yy" in z:
        sys.exit()
    if "Nn" in z:
        print ""
x = zmap.ssh_parser("{}.json".format(filename))
print "Redis Data Extraction Test"
z = zmap.redis_parser("{}.json".format(filename))


