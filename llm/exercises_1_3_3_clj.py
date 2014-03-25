from link_stack import LinkStack


def isStack(s):
    last = -1
    now = last
    stack = LinkStack(None, 0)
    for i in s:
        if i > last:
            for j in range(last + 1, i + 1):
                stack.push(j)
                print "push:", j
            last = i

        now = stack.pop()
        if i == now:
            print 'pop', now
        elif i < now:
            print "wrong"
            return

    print "right"


s = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]
isStack(s)
