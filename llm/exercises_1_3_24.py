class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def remove_after(first, node):
    if node and node.next:
        node.next = node.next.next


third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
remove_after(first, None)
j = first
while j:
    print j.item
    j = j.next

