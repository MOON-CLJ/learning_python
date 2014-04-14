import random

class RandomQueue(object):
    def __init__(self, N, capacity):
        self.N = N
        self.capacity = capacity
        self.L = [None] * capacity

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.capacity

    def enqueue(self, item):
        self.L[self.N] = item
        self.N += 1
        if self.N == self.capacity:
            self.resize(2*self.capacity)

    def dequeue(self):
        swap_index = random.choice(range(self.N))
        item = self.L[swap_index]
        self.L[swap_index] = self.L[self.N-1]
        self.L[self.N-1] = item
        self.N -= 1
        if self.N > 0 and self.N == self.capacity/4:
            self.resize(self.capacity/2)
        return item

    def sample(self):
        item = random.choice(self.L[:self.N])
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

    def random_iter(self):
        L_new = [self.L[i] for i in range(self.N)]
        random.shuffle(L_new)
        for i in L_new:
            yield i



def test(s):
    link = RandomQueue(0, 2)
    for i in s:
        if i == "-":
            print link.dequeue()
            print "link.sample:", link.sample()
            print_item(link)
        else:
            link.enqueue(i)
            print_item(link)
    print_item(link)
    print link.size()
    s_new = []
    for i in link.random_iter():
        s_new.append(i)

    print "random_iter:", s_new


def print_item(link):
    s= []
    for i in link:
        s.append(i)
    print s

if __name__ == "__main__":
    s = ["a", "b", "c", "d", "-", "e", "-", "-", "-", "f","-", "g"]
    test(s)
