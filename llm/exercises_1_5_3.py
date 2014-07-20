class WeightedQuickUnion(object):
    def __init__(self, N):
        self.N = N
        self.id = [None]*N
        self.sz = [1] * N
        for i in range(0, N):
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
        if self.sz[p_root_id] < self.sz[q_root_id]:
            self.id[p_root_id] = q_root_id
            self.sz[q_root_id] += self.sz[p_root_id]
        else:
            self.id[q_root_id] = p_root_id
            self.sz[p_root_id] += self.sz[q_root_id]
        self.times += 1
        self.count -= 1


def print_item(p, q):
    global weighted_quick_union
    print p," ", q, "  ",
    for i in weighted_quick_union.id:
        print i," ",
    print weighted_quick_union.times
    print "        ",
    for i in weighted_quick_union.sz:
        print i," ",
    print
    print


ints = [(9, 0), (3, 4), (5, 8), (7,2), (2, 1), (5, 7), (0, 3), (4, 2), (0, 1)]
weighted_quick_union = WeightedQuickUnion(10)
print "p   q    0   1   2   3   4   5   6   7   8   9   times"
print "--------------------------------------------------------"


for i in ints:
    p = i[0]
    q = i[1]
    if weighted_quick_union.connected(p, q):
        print_item(p, q)
        continue
    weighted_quick_union.union(p, q)
    print_item(p, q)


