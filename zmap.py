__author__ = "gdl"
from os import popen as execute
from sys import exit as Exit
import sys
import json
import os

try:
    prefix = os.environ['ZMAP']
except KeyError:
        prefix = "bin/zmap"
print "Using [{}]".format(prefix)

def ssh_parser(file):
    with open(file) as fh:
        for line in fh:
                if "saddr" in line:
                    x = json.loads(line)
                    z = x['saddr']
                    print z
                    import ssh
                    ssh.ssh_check(z)


def ssl_parser(filename):
    with open(filename) as fh:
        for line in fh:
                if "saddr" in line:
                    x = json.loads(line)
                    z = x['saddr']
                    print z
                    import sslscan
                    try:
                        y = sslscan.ssl_check(z)
                        sslscan.ssl_fingerprint(z)
                    except ValueError:
                        print "SSL Cert Error!"
                        pass

def ip_get(ip):
    import redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_data = r.get(ip)
    return redis_data

def redis_keys():
     import redis
     r = redis.StrictRedis(host='localhost', port=6379, db=0)
     keys = r.keys("*")
     return keys

def redis_parser(filename):
    spk = []
    with open(filename) as fh:
        for line in fh:
                if "saddr" in line:
                    x = json.loads(line)
                    z = x['saddr']
                    print "[{}]".format(z)
                    ip_get(z)
                    spk.append(redis_data)
    return spk
def privcheck():
    x = execute("whoami").read()
    if "root" in x:
        pass
    if "root" not in x:
        print "Run as root"
        z = raw_input("Run Data Analytics: [Y/N]")
        if "Yy" in z:
            pass
        if "Nn" in z:
            Exit()
def Zmaplistprobes():
    x = execute("{0} --list-probe-modules".format(prefix)).read()
    return x

def Zmaplistoutput():
    x = execute("{0} --list-output-modules".format(prefix)).read()
    return x
def Zmaptcpscan(output,port,ip=0,count=0):
    if count > 0 and ip == 0:
        privcheck()
        x = execute("sudo {0} -M tcp_synscan -N {1} -p {2} -O json -o {3}.json --output-filter='success = 1 && repeat = 0' -f saddr,success".format(prefix,
                                                                                       count,
                                                                                       port,
                                                                                       output)).read()
        return x
    if count > 0 and ip > 0:
        privcheck()
        x = execute("sudo {0} -M tcp_synscan -N {1} -p {2} {3} -O json -o {4}.json".format(prefix,
                                                                                           count,
                                                                                           port,
                                                                                           ip,
                                                                                           output)).read()
        return x
    if ip > 0:
        privcheck()
        x = execute("sudo {0} -M tcp_synscan {1} -p {2} -O json -o -".format(prefix, ip, port)).read()
        return x
    if ip == 0:
        privcheck()
        x = execute("sudo {0} -M tcp_synscan -p {1}".format(prefix,port)).read()
        return x

