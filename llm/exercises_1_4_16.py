def closest_pair(L):
    L.sort()
    differ = L[len(L)-1] - L[0]
    low = 0
    pair = []
    while low < len(L)-1:
        differ_next = L[low+1] - L[low]
        if differ_next < differ:
            differ = differ_next
            pair = [(L[low], L[low+1])]
        elif differ_next == differ:
            pair.append((L[low], L[low+1]))
        low += 1
    return pair

L = [-3, -2, 0, 5, 2, 3]
pair = closest_pair(L)
for i in pair:
    print i,
