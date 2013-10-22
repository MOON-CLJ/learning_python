import sys
import urllib2
import cPickle as pickle

s = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
l = pickle.loads(s)
for i in l:
    for k, v in i:
        sys.stdout.write(k * v)
    print
