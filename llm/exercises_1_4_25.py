def confirm_space():
    k = 1
    while k * (k+1) / 2 < N:
        k += 1
    print k
    return k

def confirm_floors(k):
    low = 0
    high = k
    while high <= N and k > 0:
        print "space = (%s, %s)"%(low+1, high)
        egg_state = raw_input("1:well, 0:broken. Enter 1 or 0:")
        if egg_state == "1":
            low += k
            k -=1
            high += k
        else:
            return low+1, high
def confirm(low, high):
    while low < high:
        egg_state = raw_input("1:well, 0:broken. Enter 1 or 0:")
        if egg_state == "1":
            low += 1
        else:
            break
    return low


N = 100
k = confirm_space()
low, high = confirm_floors(k)
print confirm(low, high)


