def guess(base, min_, max_):
    i = 0
    guess_number = min(base + 2 ** i - 1, max_)
    while guess_number <= max_:
        print min_, max_, guess_number
        if guess_number == ans:
            print 'done', guess_number
            return
        else:
            flag = raw_input("Enter hot or cold:")
            if flag == "hot" and guess_number < max_:
                i += 1
                guess_number = min(base + 2 ** i - 1, max_)
            elif flag == "hot" and guess_number == max_:
                min_ = (base + 2 ** (i - 1) - 1 + max_) / 2
                max_ -= 1
                base = min_
                guess(base, min_, max_)
            else:
                min_ = (base + 2 ** (i - 2) - 1 + base + 2 ** (i - 1) - 1) / 2
                max_ = base + 2 ** (i - 1) - 1 + guess_number
                if max_ % 2 == 0:
                    max_ = max_ / 2 - 1
                else:
                    max_ = max_ / 2
                base = min_
                guess(base, min_, max_)


N = 32
while True:
    ans = int(raw_input("Enter a number not big than %s:" % N))
    if 0 < ans <= N:
        break
    else:
        print "please enter right number!"
guess(1, 1, N)
