class DoubleNode(object):
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next

def insert_at_beginning(item, first):
    old_first = first
    first = DoubleNode(item, None, old_first)
    if old_first:
        old_first.prev = first
    return first

def insert_at_end(item, first):
    i = first
    if i:
        while i.next:
            i = i.next
        last = DoubleNode(item, i, None)
        i.next = last
    else:
        first = DoubleNode(item, None, None)
    return first


def remove_from_beginning(first):
    if first:
        first = first.next
        if first:
            first.prev = None
    return first

def remove_from_end(first):
    i = first
    if i:
        while i.next:
            i = i.next
        if i.prev:
            i.prev.next = None
        else: first = None
    return first

# when insert before "first", whether to have return expression or not
def insert_before_node(node, item):
    insert_node = DoubleNode(item, node.prev, node)
    if node.prev:
        node.prev.next = insert_node
    node.prev = insert_node

def insert_after_node(node, item):
    insert_node = DoubleNode(item, node, node.next)
    if node.next:
        node.next.prev = insert_node
    node.next = insert_node

def remove(node):
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev


first = None
first = insert_at_beginning("a", first)
#insert_at_end("b", first)
second = first.next
#insert_after_node(second, "c")
#insert_before_node(first, "1")
#i = remove_from_end(first)
#remove(second)
i = remove_from_beginning(first)
print remove_from_beginning(None)
print remove_from_end(None)
#i = first
while i:
    print i.item
    i = i.next

