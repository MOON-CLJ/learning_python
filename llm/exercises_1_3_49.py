from link_stack import LinkStack

class QueueWithStack(object):
    def __init__(self, stack_1, stack_2):
        self.stack_1 = stack_1
        self.stack_2 = stack_2

    def is_empty(self):
        return self.stack_1.isEmpty() and self.stack_2.isEmpty()

    def size(self):
        return self.stack_1.size() + self.stack_2.size()

    def enqueue(self, item):
        stack_1.push(item)

    def dequeue(self):
        if self.stack_2.isEmpty():
            while not self.stack_1.isEmpty():
                self.stack_2.push(self.stack_1.pop())
        if not self.stack_2.isEmpty():
            return self.stack_2.pop()

    def __iter__(self):
        s_1 = []
        s_2 = []
        if not self.stack_2.isEmpty():
            for i in stack_2:
                s_1.append(i)
        if not self.stack_1.isEmpty():
            for i in stack_1:
                s_2.insert(0, i)
        s = s_1 + s_2
        for i in s:
            yield i


stack_1 = LinkStack(None, 0)
stack_2 = LinkStack(None, 0)
q_with_s = QueueWithStack(stack_1, stack_2)
s = ["to", "be", "or", "not", "to", "-", "be", "-", "-", "-", "that","-", "-", "is"]
for i in s:
    if i == "-":
        q_with_s.dequeue()
    else:
        q_with_s.enqueue(i)
for i in q_with_s:
    print i ,
print
print "the number of q_with_s.Items is", q_with_s.size()


