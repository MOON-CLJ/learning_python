class RingBuffer(object):
    def __init__(self, first_index, last_index, size):
        self.first_index = first_index
        self.last_index = last_index
        self.size = size
        self.L = [None] * size

    def is_empty(self):
        return self.first_index == self.last_index 

    def is_full(self):
        return self.first_index < self.last_index and self.last_index % self.size == self.first_index % self.size

    def enqueue(self, item):
        if not self.is_full():
            self.L[self.last_index % self.size] = item
            self.last_index += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.L[self.first_index % self.size]
            self.L[self.first_index % self.size] = None
            self.first_index += 1
            return item

    def __iter__(self):
        for i in range(self.first_index, self.last_index):
            yield self.L[i % self.size] 



def test(s):
    ringbuffer = RingBuffer(0, 0, 4)
    for i in s:
        if i == "-":
            ringbuffer.dequeue()
            print "*******************dequeue***********"
            print_item(ringbuffer)
            print "first_index:", ringbuffer.first_index
            print "last_index:",ringbuffer.last_index
            print "is_empty:", ringbuffer.is_empty()
            print "is_full:", ringbuffer.is_full()
        else:
            ringbuffer.enqueue(i)
            print "*********************enqueue**********"
            print_item(ringbuffer)
            print "first_index:", ringbuffer.first_index
            print "last_index:",ringbuffer.last_index
            print "is_empty:", ringbuffer.is_empty()
            print "is_full:", ringbuffer.is_full()


    print_item(ringbuffer)


def print_item(ringbuffer):
    s= []
    for i in ringbuffer:
        s.append(i)
    print s

if __name__ == "__main__":
    s = ["a", "b", "c", "d", "-", "e", "-", "-", "-", "-", "f","-", "g"]
    test(s)
