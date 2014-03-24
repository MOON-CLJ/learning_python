class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkBag(object):
    def __init__(self, first):
        self.first = first
    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
    def __iter__(self):
        while self.first is not None:
            item = self.first.item
            self.first = self.first.next
            yield item


def test(s):
    link = LinkBag(None)
    for i in s:
        link.add(i)
    for i in link:
        print i


s = ["we", "are", "student", "."]
test(s)
