class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class CircularQueue(object):
    def __init__(self, last, N):
        self.last = last
        self.N = N

    def size(self):
        return self.N

    def isEmpty(self):
        return self.last is None

    def enqueue(self, item):
        if self.isEmpty():
            self.last = Node(item, None)
            self.last.next= self.last
        else:
            self.last.next = Node(item, self.last.next)
            self.last = self.last.next
        self.N += 1

    def dequeue(self):
        item = self.last.next.item
        if self.size() == 1:
            self.last = None
        else:
            self.last.next = self.last.next.next
        self.N -= 1
        return item

    def __iter__(self):
        count = self.size()
        now = self.last.next
        while count > 0:
            item = now.item
            now = now.next
            count -= 1
            yield item


def test(s):
    link  =CircularQueue(None, 0)
    for i in s:
        if i == "-":
            print "--------------", link.dequeue()
        else:
            link.enqueue(i)
            print "+++++++++++++++", i
    print_item(link)


def print_item(link):
    s= []
    for i in link:
        s.append(i)
    print s
    print "the number of link.Items is", link.N


s = ["to", "be", "or", "not", "to", "-", "be", "-", "-", "-", "that", "-", "is"]
test(s)
