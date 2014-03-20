class Stack(object):
    def __init__(self, N):
        self.N = N
        self.L = [None] * N

    def is_empty(self):
        return self.N ==0
    def size(self):
        return self.N

    def push(self, s):
        L[self.N] = s
        self.N += 1

    def pop(self):
        self.N -= 1
        return L[self.N+1]
