def faster_merge(a, lo, mid, hi):
    aux = []
    for i in a[mid + 1: hi + 1]:
        aux.insert(0, i)
    N = len(aux)
    k = N - 1
    i = lo
    flag = 0
    while i < mid + 1:
        if k < 0:
            return flag
        if a[mid] < a[mid + 1]:
            return flag
        count = 1
        if less(aux[k], a[i]):
            while k - count >= 0 and less(aux[k - count], a[i]):
                count += 1
            for j in range(mid + count, i + count - 1, -1):
                a[j] = a[j - count]
            mid += count
            for j in range(i, i + count):
                a[j] = aux[k - (j - i)]
                if k - (j - i) == N - 1 :
                    flag = j
            k -= count
        i += count
        print i, a, aux
    return flag    


def less(p, q):
    return p < q
if __name__ == '__main__':
    #a = [1, 3, 7, 8, 10, 6, 11, 12]
    a = [0, 6, 7, 8, 9, 11, 12, 13, 1, 2, 3, 4, 10, 14]
    hi = len(a) - 1
    lo = 0
    flag = faster_merge(a, lo, 7, hi)
    print a, flag



