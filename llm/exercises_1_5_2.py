class QuickUnion(object):
    def __init__(self, N):
        self.N = N
        self.id = [None]*N
        for i in range(N):
            self.id[i] = i
        self.count = N
        self.times = 0

    def find(self, p):
        self.times += 1
        while p != self.id[p]:
            p = self.id[p]
            self.times += 2
        return p

    def connected(self, p, q):
        self.times = 0
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root_id = self.find(p)
        q_root_id = self.find(q)
        if p_root_id == q_root_id:
            return
        self.id[p_root_id] = q_root_id
        self.times += 1
        self.count -= 1


def print_item(p, q):
    global quick_union
    print p," ", q, "  ",
    for i in quick_union.id:
        print i," ",
    print quick_union.times
    print


ints = [(9, 0), (3, 4), (5, 8), (7,2), (2, 1), (5, 7), (0, 3), (4, 2), (0, 1)]
quick_union = QuickUnion(10)
print "p   q    0   1   2   3   4   5   6   7   8   9   times"
print "--------------------------------------------------------"


for i in ints:
    p = i[0]
    q = i[1]
    if quick_union.connected(p, q):
        print_item(p, q)
        continue
    quick_union.union(p, q)
    print_item(p, q)




