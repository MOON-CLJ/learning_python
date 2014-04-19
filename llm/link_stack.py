class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkStack(object):
    def __init__(self, first, N):
        self.N = N
        self.first = first
        self.count = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def push(self, item):
        oldNode = self.first
        self.first = Node(item, oldNode)
        self.N += 1
        self.count += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        self.count += 1
        return item

    def peek(self):
        return self.first.item

    def __iter__(self):
        num = self.count
        now = self.first
        while now:
            print "num:", num, "self.count", self.count
            if num == self.count:
                item = now.item
                now = now.next
                yield item
            else:
                print "wrong"
                return


def test(s):
    link = LinkStack(None, 0)
    for i in s:
        if i == "-":
            link.pop()
        else:
            link.push(i)
    print_item(link)


def print_item(link):
    for i in link:
        if i == "is":
            link.pop()
        else:
            print i,
    print
    print "the number of link.Items is", link.size()


if __name__ == "__main__":
    s = ["to", "be", "or", "not", "to", "-", "be", "-", "-", "-", "that","-", "-", "is"]
    test(s)


