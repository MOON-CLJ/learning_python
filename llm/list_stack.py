class Stack(object):
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.L = [None] * M

    def is_empty(self):
        return self.N ==0

    def size(self):
        return self.N

    def push(self, s):
        self.L[self.N] = s
        self.N += 1

    def pop(self):
        self.N -= 1
        return self.L[self.N]

    def isFull(self):
        return self.N == self.M


def test(s):
    stack = Stack(0, 5)
    for i in s:
        if i == "-":
            print stack.pop()

        else:
            stack.push(i)
            print i, stack.N, "*************", stack.L
    print stack.L, stack.size()



s = ["it", "was", "-", "the", "best", "-", "of", "times", "-", "-", "-", "it", "was", "-", "the", "-", "-"]
test(s)
