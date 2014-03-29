class Node():
    def __init__(self, item, next):
        self.item = item
        self.next = next


def delete(first, k):
    i = first
    j = 1
    if k == 1:
        first = first.next
    elif k <= size(first):
        while j < k - 1:
            i = i.next
            j += 1
        i.next = i.next.next
    return first
   
def size(first):
    i = first
    j = 0
    while i:
        i = i.next
        j += 1
    return j
   
third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
j = delete(first, 1)
while j:
    print j.item
    j = j.next

