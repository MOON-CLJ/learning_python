class QuickFind(object):
    def __init__(self, N):
        self.N = N
        self.count = N
        self.id = [None]*N
        for i in range(0, N):
            self.id[i] = i
        self.times = 0

    def connected(self, p, q):
        self.times = 0
        return self.find(p) == self.find(q)

    def find(self, p):
        self.times += 1
        return self.id[p]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        for i in range(0, self.N):
            self.times += 1
            if self.id[i] == p_id:
                self.id[i] = q_id
                self.times += 1
        self.count -= 1


def print_item(p, q):
    global quick_find
    print p," ", q, "  ",
    for i in quick_find.id:
        print i," ",
    print quick_find.times
    print

ints = [(9, 0), (3, 4), (5, 8), (7,2), (2, 1), (5, 7), (0, 3), (4, 2), (0, 1)]
quick_find = QuickFind(10)
print "p   q    0   1   2   3   4   5   6   7   8   9   times"
print "--------------------------------------------------------"


for p, q in ints:
    if quick_find.connected(p, q):
        print_item(p, q)
        continue
    quick_find.union(p, q)
    print_item(p, q)



