from link_stack import LinkStack

def copy_stack(s):
    r = LinkStack(None, 0)
    temple = []
    for i in s:
        temple.insert(0, i)
    for i in temple:
        r.push(i)
    return r


s = LinkStack(None, 0)
for i in range(10):
    s.push(i)
r = copy_stack(s)

r.pop()
for i in r:
    print i,

print
print "*************divide************"

for i in s:
    print i,


