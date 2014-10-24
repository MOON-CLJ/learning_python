import functools


class Node(object):
    def __init__(self, item):
        self.item = item
        self.dep = None


def build_dep():
    l = [Node(i) for i in range(21)]
    l[0].dep = [l[1], l[6], l[11], l[16]]
    for i in range(1, 21):
        if i % 5 != 0:
            l[i].dep = [l[i + 1]]
    return l


def gather_dep_by_recursion(l):
    ordered = [l.item]
    if l.dep is None:
        return ordered
    for i in l.dep:
        ordered.extend(gather_dep_by_recursion(i))
    return ordered


def gather_dep_by_queue(l):
    ordered = []
    q = [l]
    while q:
        tmp = q.pop()
        if tmp.dep:
            for i in tmp.dep:
                q.insert(0, i)
        ordered.append(tmp.item)
    return ordered


if __name__ == "__main__":
    a = build_dep()
    print gather_dep_by_recursion(a[0])
    print gather_dep_by_queue(a[0])
