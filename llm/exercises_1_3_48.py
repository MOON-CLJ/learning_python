from link_stack import LinkStack

class Deque(object):
    def __init__(self, stack_1, stack_2):
        self.stack_1 = stack_1
        self.stack_2 = stack_2

    def size(self):
        return self.stack_1.size() + self.stack_2.size()

    def isEmpty(self):
        return self.stack_1.isEmpty() and self.stack_2.isEmpty()

    def push_left(self, item):
        self.stack_1.push(item)

    def push_right(self, item):
        self.stack_2.push(item)

    def pop_left(self):
        if self.stack_1.isEmpty():
            while not self.stack_2.isEmpty():
                self.stack_1.push(self.stack_2.pop())
        if not self.stack_1.isEmpty():
            return self.stack_1.pop()

    def pop_right(self):
        if self.stack_2.isEmpty():
            while not self.stack_1.isEmpty():
                self.stack_2.push(self.stack_1.pop())
        if not self.stack_2.isEmpty():
            return self.stack_2.pop()

    def __iter__(self):
        s_1 = []
        s_2 = []
        if not self.stack_1.isEmpty():
            for i in self.stack_1:
                s_1.append(i)
        if not self.stack_2.isEmpty():
            for i in self.stack_2:
                s_2.insert(0, i)
        s = s_1 + s_2
        for i in s:
            yield i


def test(s):
    stack_1 = LinkStack(None, 0)
    stack_2 = LinkStack(None, 0)
    deque = Deque(stack_1, stack_2)
    for i in s:
        if i == "-":
            deque.pop_left()
            print_item(deque)
        elif i == "*":
            deque.pop_right()
            print_item(deque)
        elif i in range(10):
            deque.push_left(i)
            print_item(deque)
        else:
            deque.push_right(i)
            print_item(deque)
    print_item(deque)
    

def print_item(deque):
    s= []
    for i in deque:
        s.append(i)
    print s, deque.size()


s = ["a", "b", "c", 1, 2, "-", "d", "*", "*", "-", 3, "-", "*", "e"]
test(s)





