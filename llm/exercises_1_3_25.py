class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def insert_after(node_1, node_2):
    if node_1 and node_2:
        node_2.next = node_1.next
        node_1.next = node_2


third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
insert_after(first, Node("d", None))
j = first
while j:
    print j.item
    j = j.next

