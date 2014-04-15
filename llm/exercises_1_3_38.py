class GeneralizedQueueString(object):
    def __init__(self, N, capacity):
        self.N = N
        self.capacity = capacity
        self. L = [None] * capacity

    def is_empty(self):
        return self.N == 0

    def insert(self, item):
        self.L[self.N] = item
        self.N += 1
        if self.N == self.capacity:
            self.resize(2*self.capacity)

    def delete(self, kth):
        if kth <= self.N:
            item = self.L[self.N - kth]
            for i in range(self.N - kth, self.N-1):
                self.L[i] = self.L[i+1]
            self.N -= 1
            if self.N > 0 and self.N == self.capacity/4:
                self.resize(self.capacity/2)
            return item

    def resize(self, capacity_new):
        L_new = [None] * capacity_new
        for i in range(min(self.N, capacity_new)):
            L_new[i] = self.L[i]
        self.L = L_new
        self.capacity = capacity_new

    def __iter__(self):
        for i in self.L[:self.N]:
            yield i


class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next
class GeneralizedQueueLink(object):
    def __init__(self, first, last, N):
        self.first = first
        self.last = last
        self.N = N

    def is_empty(self):
        return self.first is None

    def insert(self, item):
        oldlast = self.last
        self.last = Node(item, None)
        if oldlast:
            oldlast.next = self.last
        if self.is_empty():
            self.first = self.last
        self.N += 1

    def delete(self, kth):
        now = self.first
        if kth <= self.N:
            if kth == self.N:
                item = self.first.item
                self.first = self.first.next
                if self.is_empty():
                    self.last = None
            else:
                while kth < self.N -1:
                    now = now.next
                    kth += 1
                item = now.next.item
                now.next = now.next.next
            self.N -= 1
            return item

    def __iter__(self):
        now = self.first
        while now:
            item = now.item
            now = now.next
            yield item

    
g_queue = GeneralizedQueueString(0, 10)
for i in range(10):
    g_queue.insert(i)
for i in g_queue:
    print i,
print 
print "delete item:", g_queue.delete(4)
print g_queue.is_empty()
print "*************************divide******************"
l_queue = GeneralizedQueueLink(None, None, 0)
for i in range(10):
    l_queue.insert(i)
for i in l_queue:
    print i,
print
print "delete item link:", l_queue.delete(4)
print l_queue.is_empty()
