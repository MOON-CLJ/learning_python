from exercises_1_3_29 import CircularQueue

def josephus(N, M):
    circle_queue = CircularQueue(None, 0)
    for i in range(N):
        circle_queue.enqueue(i)
    first = circle_queue.last
    count = N
    while count > 0:
        times = 0
        while times < M-1:
            first = first.next
            times += 1
        print first.next.item,
        first.next = first.next.next
        count -= 1


josephus(7, 2)


