class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


def max(first):
    if first:
        max_val = first.item
        i = first
        while i.next:
            if i.next.item > max_val:
                max_val = i.next.item
            i = i.next
        return max_val
    else:
        return 0


def max_recursive(node):
    if node:
        if node.next:
            if node.next.item > node.item:
                return max_recursive(node.next)
            else:
                node.next = node.next.next
                return max_recursive(node)
        else:
            return node.item
    else:
        return 0


def max_recursive_new(node):
    global max
    if node:
        if node.item > max:
            max = node.item
        return max_recursive_new(node.next)
    else:
        return 0

third = Node(18, None)
second = Node(20, third)
first = Node(30, second)
print "methode general:", max(first)
print "methode recursive:", max_recursive(first)
max = 0
max_recursive_new(first)
print "methode recursive new:", max

