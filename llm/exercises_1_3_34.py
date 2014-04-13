import random

class RandomBag(object):
    def __init__(self, N, M):
        self.M = M
        self.N = N
        self.L = [None]*M

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.M

    def add(self, item):
        for i in range(self.N):
            if self.L[i] == item:
                return
        self.L[self.N] = item
        self.N += 1
        if self.N == self.M:
            self.resize(2*self.M)

    def resize(self, capacity_new):
        L_new = [None] * capacity_new
        for i in range(min(self.N, capacity_new)):
            L_new[i] = self.L[i]
        self.L = L_new
        self.M = capacity_new

    def __iter__(self):
        L_new = [self.L[i] for i in range(self.N)]
        random.shuffle(L_new)
        for i in L_new:
            yield i

        
random_bag = RandomBag(0, 1)
random_bag.add("a")
random_bag.add("b")
random_bag.add("b")
for i in random_bag:
    print i
print "**********", random_bag.size()
