def two_sum_faster(L1, L2):
    low_1 = 0
    high_2 = len(L2) - 1
    count = 0
    while low_1 < len(L1) and high_2 >= 0:
        if L1[low_1] + L2[high_2] > 0:
            high_2 -= 1
        elif L1[low_1] + L2[high_2] < 0:
            low_1 += 1
        else:
            count_L1 = 1
            count_L2 = 1
            low_1 += 1
            high_2 -= 1
            while low_1 < len(L1) and L1[low_1] == L1[low_1 - 1]:
                count_L1 += 1
                low_1 += 1
            while high_2 >= 0 and L2[high_2] == L2[high_2 + 1]:
                count_L2 += 1
                high_2 -= 1
            count += count_L1 * count_L2
    return count

#L1 = [1, 1, 2, 2, 3, 5]
#L2 = [-4, -3, -2, -2, -1, -1]
L1 = [-1, -1, 0, 1, 1]
L2 = [-1, 0, 1, 1]
print two_sum_faster(L1, L2)
