from os import popen as execute
from sys import exit as Exit
import redis
def ssh_check(ip):
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        import GIS
        GIS.GIS(ip)
        x = execute("ssh-keyscan {0}".format(ip)).read()
        r.set(name=ip,value=x)
        print x
        return x
    except KeyboardInterrupt:
        z = raw_input("Quit Scan [Y/N]: ")
        if "Yy" in z:
            Exit() and exit()
        if "Nn" in z:
            pass