class Node():
    def __init__(self, item, next):
        self.item = item
        self.next = next


def delete(first, k):
    i = first
    j = 1
    if k == 1:
        first = first.next
    else:
        while (j < k - 1 and i.next):
            i = i.next
            j += 1
        if i.next:
            i.next = i.next.next
    return first


third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
j = delete(first, 3)
while j:
    print j.item
    j = j.next
