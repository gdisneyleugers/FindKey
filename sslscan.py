from os import popen as execute
from sys import exit as Exit
import redis
import json
def ssl_check(ip):
    try:
        import grc
        z = grc.fetch_server_certificate(ip,443)
        print z
    except KeyboardInterrupt:
        z = raw_input("Quit Scan [Y/N]: ")
        if "Yy" in z:
            Exit()
        if "Nn" in z:
            pass
    except OSError:
        print "Fetch Error!"
        pass

def ssl_fingerprint(ip):
    spacer = "============================================="
    print spacer
    x = execute("openssl x509 -fingerprint -in {0}.pem -pubkey -noout".format(ip)).read()
    nn = "[{0}.pem]: {1}".format(ip,x)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set(name=ip,value=x)
    print nn
    print spacer