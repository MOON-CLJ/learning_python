class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def reverse_iterative(node):
    reverse_node = None
    first = node
    while first is not None:
        second = first.next
        first.next = reverse_node
        reverse_node = first
        first = second
    return reverse_node


def reverse_recursive(first, reverse_node):
    if first is None:
        return reverse_node
    else:
        first_next = first.next
        first.next = reverse_node
        reverse_node = first
        return reverse_recursive(first_next, reverse_node)

third = Node("c", None)
second = Node("b", third)
first = Node("a", second)
print "&&&&&&&&&&&&&&&&&&&&&&& iterative method &&&&&&&&&&&&&&&&&&&&&&"
j = reverse_iterative(first)
node = j
while j:
    print j.item
    j = j.next
print first.next is None, second.item, third.next is None

print "************************recursive method**********************"
k = reverse_recursive(node, None)
while k:
    print k.item
    k = k.next
print first.next is None, second.item, third.next is None





        
