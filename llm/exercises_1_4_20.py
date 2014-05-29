# search maxvlaue_index
def bitonic_search_max(low, high):
    while low < high:
        middle = (low + high)/2
        if high - low > 1:
            if L[middle-1] < L[middle] and L[middle] > L[middle+1]:
                return middle
            elif L[middle-1] < L[middle] < L[middle+1]:
                low = middle
            else:
                high = middle
        else:
            if L[low] > L[high]:
                return low
            else:
                return high


# bisection search
def bisection_search(low, high, v, flag):
    while low <= high:
        middle = (low + high)/2
        if v < L[middle]:
            if flag == "increase":
                high = middle - 1
            else:
                low = middle + 1
        elif v > L[middle]:
            if flag == "increase":
                low = middle + 1
            else:
                high = middle -1
        else:
            return middle


# test
def test(L):
    high = len(L)-1
    v = raw_input("Enter a search number:")
    v = int(v)
    maxvalue_index = bitonic_search_max(0, high)
    R1 = bisection_search(0, maxvalue_index, v, "increase")
    if R1 is not None:
        print R1
        return
    R2 = bisection_search(maxvalue_index+1, high, v, "decrease")
    if R2 is not None:
        print R2
    else:
        print "can't find the value in the arry"


L = [0, 2, 5, 6, 7, 9, 10, 8, 3, 1]
test(L)


