class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkBag(object):
    def __init__(self, first, N):
        self.first = first
        self.N = N

    def add(self, item):
        i = self.first
        while i:
            if item == i.item:
                return
            else:
                i = i.next
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.N += 1
    
    def __iter__(self):
        now = self.first
        while now:
            item = now.item
            now = now.next
            yield item


def test(s):
    link = LinkBag(None, 0)
    for i in s:
        link.add(i)
    for i in link:
        print i


s = ["we", "we", "student", "."]
test(s)
