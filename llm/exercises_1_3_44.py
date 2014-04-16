from link_stack import LinkStack

class Buffer(object):
    
    def __init__(self, stack_1, stack_2):
        self.stack_1 = stack_1
        self.stack_2 = stack_2

    def insert(self, char):
        self.stack_1.push(char)

    def delete(self):
        if not self.stack_1.isEmpty():
            return self.stack_1.pop()

    def left(self, k):
        k_new = min(k, self.stack_1.size())
        for i in range(k_new):
            self.stack_2.push(self.stack_1.pop())

    def right(self, k):
        k_new = min(k, self.stack_2.size())
        for i in range(k_new):
            self.stack_1.push(self.stack_2.pop())

    def size(self):
        N = self.stack_1.size() + self.stack_2.size()
        return N

    def __iter__(self):
        s_1 = ["|"]
        s_2 = []
        for i in self.stack_1:
            s_1.insert(0, i)
        for i in self.stack_2:
            s_2.append(i)
        s = s_1 + s_2
        for i in s:
            yield i


stack_1 = LinkStack(None, 0)
stack_2 = LinkStack(None, 0)
buffer = Buffer(stack_1, stack_2)
for i in range(10):
    buffer.insert(i)

buffer.delete()
buffer.left(4)
buffer.right(3)
print "size:", buffer.size()
for i in buffer:
    print i,

        
