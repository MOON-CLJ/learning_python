class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def find_key(first, k):
    i = first
    while i:
        if i.item == k:
            return True
        i = i.next
    return False


third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
j = find_key(first, "b")
print j

