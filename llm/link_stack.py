class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkStack(object):
    def __init__(self, first, N):
        self.N = N
        self.first = first
      
    def isEmpty(self):
        return self.first is None
            

    def size(self):
        return self.N

    def push(self, item):
        oldNode = self.first
        self.first = Node(item, oldNode)
        self.N += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        return item  


def test(s):
    link = LinkStack(None, 0)
    for i in s:
        if i == "-":
            link.pop()
        else:
            link.push(i)
    print_item(link)
    

def print_item(link):
    length = link.N
    s= []
    for i in range(length):
        item = link.first.item
        link.first = link.first.next
        s.append(item)
    print s
    print "the number of link.Items is", link.N


s = ["to", "be", "or", "not", "to", "-", "be", "-", "-", "-", "that","-", "-", "is"]
test(s)


