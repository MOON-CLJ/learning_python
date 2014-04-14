class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

def move_to_front(char, first):
    now = first
    if not now:
        first = Node(char, None)
        return first
    if char == now.item:
        return first
    while now.next:
        if now.next.item == char:
            now.next = now.next.next
            break
        else:
            now = now.next
    oldfirst = first
    first = Node(char, oldfirst)
    return first
  

s = ["a", "b", "a", "c", "b", "a"]
first = None
for i in s:
    first = move_to_front(i, first)

now = first
while now:
    print now.item,
    now = now.next

