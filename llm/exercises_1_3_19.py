class Node():
    def __init__(self, item, next):
        self.item = item
        self.next = next


def remove_node(first):
    i = first
    while i.next.next:
        i = i.next
    i.next = None


third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
remove_node(first)
j = first
while j:
    print j.item
    j = j.next

