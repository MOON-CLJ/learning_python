def local_min_matrix(low_row, high_row, low_col, high_col):
    middle_row = (low_row + high_row)/2
    middle_col = (low_col + high_col)/2
    v = L[middle_row][middle_col]
    if high_row - low_row > 1 and high_col - low_col > 1:
        v_pre =  L[middle_row][middle_col-1] 
        v_next = L[middle_row][middle_col+1] 
        v_up = L[middle_row-1][middle_col] 
        v_down =  L[middle_row+1][middle_col] 
        if v < v_next and v < v_pre and v < v_up and v < v_down:
            return middle_row, middle_col
        else:
            if v < v_next:
                r = local_min_matrix(low_row, high_row, middle_col+1, high_col)
            else:
                r = local_min_matrix(low_row, high_row, middle_col, high_col)
            if r is not None:
                return r
            if v < v_pre:
                r = local_min_matrix(low_row, high_row, low_col, middle_col-1)
            else:
                r = local_min_matrix(low_row, high_row, low_col, middle_col)
            if r is not None:
                return r
            if v < v_up:
                r = local_min_matrix(low_row, middle_row-1, low_col, high_col)
            else:
                r = local_min_matrix(low_row, middle_row, low_col, high_col)
            if r is not None:
                return r
            if v < v_down:
                r = local_min_matrix(middle_row+1, high_row, low_col, high_col)
            else:
                r = local_min_matrix(middle_row, high_row, low_col, high_col)
            if r is not None:
                return r

L = [[6, 2, 3, 16, 17, 18], [7, 8, 9, 19, 20, 21], [13, 14, 15, 22, 23, 24], [4, 1, 5, 25, 26, 27], [10, 11, 12, 29, 30, 31]] 
high_row = len(L) - 1
high_col = len(L[0]) - 1
(row, col) = local_min_matrix(0, high_row, 0, high_col)
print "row = %s, col = %s, value = %s" %(row, col, L[row][col])


