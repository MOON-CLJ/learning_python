class ResizingArrayQueueOfString(object):
    def __init__(self, N, capacity):
        self.N = N
        self.capacity = capacity
        self.L = [None] * capacity

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.capacity

    def enqueue(self, char):
        self.L[self.N] = char
        self.N += 1
        if self.N == self.capacity:
            self.resize(2*self.capacity)

    def dequeue(self):
        item = self.L[0]
        i = 0
        while i < self.N - 1:
            self.L[i] = self.L[i+1]
            i += 1
        self.N -= 1
        if self.N > 0 and self.N == self.capacity/4:
            self.resize(self.capacity/2)
        return item

    def is_full(self):
        return self.N == self.capacity

    def resize(self, capacity_new):
        L_new = [None] * capacity_new
        for i in range(min(self.N, capacity_new)):
            L_new[i] = self.L[i]
        self.L = L_new
        self.capacity = capacity_new

    def __iter__(self):
        for i in range(self.N):
            yield self.L[i]


def test(s):
    queue_test = ResizingArrayQueueOfString(0, 8)
    for i in s:
        if i == "-":
            queue_test.dequeue()
        else:
            queue_test.enqueue(i)
    print "size", queue_test.size()
    for i in queue_test:
        print i,


s = ["it", "was", "-", "the", "best", "-", "of", "times", "-", "-", "it", "was", "-", "the", "-", "-"]
test(s)


