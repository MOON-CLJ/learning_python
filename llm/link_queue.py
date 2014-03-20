class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkQueue(object):
    def __init__(self, first, last, N):
        self.first = first
        self.last = last
        self.N = N
    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def enqueue(self, item):
        oldLast = self.last
        self.last = Node(item, None)
        if self.isEmpty():
            self.first = self.last
        else:
            oldLast.next = self.last
        self.N += 1
    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():
            self.last = None
        self.N -= 1
        return item

    
def test(s):
    link = LinkQueue(None, None, 0)
    for i in s:
        if i == "-":
            link.dequeue()
        else:
            link.enqueue(i)
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
       
