class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Steque(object):
    def __init__(self, first, last, N):
        self.first = first
        self.last = last
        self.N = N

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def push(self, item):
        old_first = self.first
        self.first = Node(item, old_first)
        if self.isEmpty():
            self.last = self.first
        self.N += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():
            self.last = None
        self.N -= 1
        return item

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item, None)
        if self.isEmpty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.N += 1

    def __iter__(self):
        now = self.first
        while now:
            item = now.item
            now = now.next
            yield item


def test(s):
    steque = Steque(None, None, 0)
    for i in s:
        if i == "-":
            steque.pop()
            print_item(steque)
        elif i in range(10):
            steque.push(i)
            print_item(steque)
        else:
            steque.enqueue(i)
            print_item(steque)
    print_item(steque)


def print_item(steque):
    s= []
    for i in steque:
        s.append(i)
    print s


s = ["a", "b", "c", 1, 2, "-", "d", "-", "-", "-", 3, "-", "-", "e"]
test(s)



