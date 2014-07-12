def confirm_range():
    global k
    while True:
        egg_state = raw_input("'1': well, '0':broken. Enter 1 or 0:")
        if egg_state == "1":
            k += 1
        else:
            return k


def bisection(k):
    low = 2 ** (k - 1)
    high = 2 ** k
    while high - low > 1:
        middle = (low + high) / 2
        print "low = %s, high = %s, middle = %s" % (low, high, middle)
        egg_state = raw_input("'1':well, '0':broken. Enter 1 or 0:")
        if egg_state == "1":
            low = middle
        else:
            high = middle
        print "(%s, %s)" % (low, high)
    return high


k = 0
k = confirm_range()
print bisection(k)
