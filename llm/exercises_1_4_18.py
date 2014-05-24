def local_min_index(low, high):

    middle = (low + high)/2
    if high - low > 1:
        if L[middle] < L[middle+1] and L[middle] < L[middle-1]:
            return middle
            
        else:
            if L[middle] > L[middle+1]:
                r = local_min_index(middle, high)
            else:
                r = local_min_index(middle+1, high)
            if r is not None:
                return r
            if L[middle] > L[middle-1]:
                r = local_min_index(low, middle)
            else:
                r = local_min_index(low, middle-1)
            if r is not None:
                return r



L = [10, 1, 2, 3, 5, 6, 7, 9, 8]
h = len(L)-1
print local_min_index(0, h)


            
