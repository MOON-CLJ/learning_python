def bisection(k, L):
    low = 0
    high = len(L) - 1
    while low < high:
        middle = (low + high) / 2 + 1
        if k < L[middle]:
            high = middle - 1
        else:
            low = middle
    if k == L[low]:
        return low
    else:
        return -1


def common_value(L1, L2):
    low_1 = 0
    low_2 = 0
    while low_1 < len(L1) and low_2 < len(L2):
        if L1[low_1] < L2[low_2]:
            index = bisection(L2[low_2], L1[low_1:])
            if index != -1:
                print L2[low_2],
                low_2 += 1
                low_1 = low_1 + index + 1
            else:
                low_2 += 1
                low_1 += 1
        elif L1[low_1] > L2[low_2]:
            index = bisection(L1[low_1], L2[low_2:])
            if index != -1:
                print L1[low_1],
                low_1 += 1
                low_2 = low_2 + index + 1
            else:
                low_1 += 1
                low_2 += 1
        else:
            print L1[low_1],
            low_1 += 1
            low_2 += 1


L1 = [1, 2, 2, 2, 5, 5, 9]
L2 = [2, 2, 4, 5, 5, 5, 9]
common_value(L1, L2)
