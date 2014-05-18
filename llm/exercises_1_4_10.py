def binary_search_by_minindex(k, L):
    low = 0
    high = len(L) - 1
    while low < high:
        middle = (low + high)/2
        if k <= L[middle]:
            high = middle
        else:
            low = middle + 1
    if k == L[low]:
        return low
    else:
        return -1


L= [1, 2, 3, 3, 3, 4, 4, 5, 5, 7, 7]
k = raw_input("Enter a searching number:")
k = int(k)
print binary_search_by_minindex(k, L)



