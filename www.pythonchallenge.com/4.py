import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
next_nothing = "12345"
s = []
while 1:
    resp = urllib2.urlopen(url % next_nothing).read()
    next_nothing = resp[-5:]
    next_nothing = next_nothing.strip()
    print next_nothing
    if next_nothing in s:
        break
    else:
        s.append(next_nothing)

print s
