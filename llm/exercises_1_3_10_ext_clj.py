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
            if not stack.isEmpty():
                last = stack.peek()
                while last != "(" and prior[last] >= prior[i]:
                    result += " %s" % stack.pop()
                    last = stack.peek()
            stack.push(i)

    while not stack.isEmpty():
        result += " %s" % stack.pop()

    print result


s = "3+(2-5*4)*6/3"
s = divide_str(s)
InfixToPostfix(s)
