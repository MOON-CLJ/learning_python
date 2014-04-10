class DoubleLink(object):
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next

class Deque(object):
    def __init__(self, first, last, N):
        self.first = first
        self.last = last
        self.N = N

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def push_left(self, item):
        old_first = self.first
        self.first = DoubleLink(item, None, old_first)
        if old_first:
            old_first.prev = self.first
        if self.isEmpty():
            self.last = self.first
        self.N += 1

    def push_right(self, item):
        old_last = self.last
        self.last = DoubleLink(item, old_last, None)
        if old_last:
            old_last.next = self.last
        if self.isEmpty():
            self.first = self.last
        self.N += 1

    def pop_left(self):
        if not self.isEmpty():
            item = self.first.item
            self.first = self.first.next
            if not self.isEmpty():
                self.first.prev = None
            else:
                self.last = None
            self.N -= 1
            return item

    def pop_right(self):
        if not self.isEmpty():
            item = self.last.item
            if self.last.prev:
                self.last.prev.next = None
            else:
                self.first = None
            self.last = self.last.prev
            self.N -= 1
            return item

    def __iter__(self):
        now = self.first
        while now:
            item = now.item
            now = now.next
            yield item


def test(s):
    deque = Deque(None, None, 0)
    for i in s:
        if i == "-":
            deque.pop_left()
            print_item(deque)
        elif i == "*":
            deque.pop_right()
            print_item(deque)
        elif i in range(10):
            deque.push_left(i)
            print_item(deque)
        else:
            deque.push_right(i)
            print_item(deque)
    print_item(deque)


def print_item(deque):
    s= []
    for i in deque:
        s.append(i)
    print s, deque.N


s = ["a", "b", "c", 1, 2, "-", "d", "*", "*", "-", 3, "-", "*", "e"]
test(s)



