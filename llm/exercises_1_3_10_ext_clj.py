from link_stack import LinkStack


prior = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}


def divide_str(s):
    l = []
    last = None
    for i in s:
        if i in ["(", ")", "+", "-", "*", "/"]:
            l.append(i)
        elif i.isdigit():
            if last and last.isdigit():
                l[-1] += i
            else:
                l.append(i)
        last = i
    return l


def InfixToPostfix(infix):
    stack = LinkStack(None, 0)
    result = ""
    for i in infix:
        if i.isdigit():
            result += " %s" % i
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while stack.peek() != "(":
                result += " %s" % stack.pop()
            stack.pop()
        else:
            while 1:
                if stack.isEmpty():
                    break
                last = stack.peek()
                if last != "(" and prior[last] >= prior[i]:
                    result += " %s" % stack.pop()
                else:
                    break
            stack.push(i)

    while not stack.isEmpty():
        result += " %s" % stack.pop()

    print result


s = "3+(2-5*4)*6/3"
s = "3+2*5-4"
s = divide_str(s)
InfixToPostfix(s)
