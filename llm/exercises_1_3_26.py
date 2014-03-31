class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def remove(first, var):
    while first.item == var:
        first = first.next
    i = first
    while i and i.next:
        if i.next.item == var:
            i.next = i.next.next
        i = i.next
    return first

   
third = Node("a", None)
second = Node("c", third)
first = Node("a", second)
j = remove(first, "a")
while j:
    print j.item
    j = j.next



