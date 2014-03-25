from link_stack import LinkStack

def isStack(s):
    last = -1
    stack = LinkStack(None, 0)
    for i in s:
        if stack.isEmpty() or i > stack.first.item:
            for j in range(last+1, i +1):
                stack.push(j)                   
                print "push:", stack.first.item
            last = stack.pop()
            print "pop:", last
        elif i == stack.first.item:
            print "pop", stack.pop()
        elif i < stack.first.item:
            print "wrong"
            return
    print "right"


s =[4, 3, 2, 1, 0, 9, 8, 7, 6, 5] 
isStack(s)
