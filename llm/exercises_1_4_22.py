def fib(max_index):
    global k
    while a[k] < max_index:
        k += 1
        a.append(a[k - 1] + a[k - 2])
    return k


def fib_search(v):
    global k
    low = 0
    while low < length:
        if k <= 1:
            if L[low] == v:
                return low
            elif L[low + 1] == v:
                return low + 1
        else:
            middle = low + a[k] - a[k - 1]
            print low, middle, low + a[k]
            print k - 2
            if v == L[middle]:
                return middle
            elif v < L[middle]:
                k -= 2
            else:
                low = middle
                k -= 1


a = [1, 1]
k = 1
#L = [1, 3, 4, 5, 6, 7]
L = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
length = len(L)
fib(length - 1)
print k
v = raw_input("Enter a searching number:")
print fib_search(int(v))
