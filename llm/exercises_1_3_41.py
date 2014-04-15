from link_queue import LinkQueue

def copy_queue(p):
    r = LinkQueue(None, None, 0)
    for i in p:
        r.enqueue(i)
    return r

pl = []
rl =[]
p = LinkQueue(None, None, 0)
for i in range(10):
    p.enqueue(i)

r = copy_queue(p)
p.dequeue()
for i in p:
    print i,
print
print "**************divide***********"
for i in r:
    print i,



