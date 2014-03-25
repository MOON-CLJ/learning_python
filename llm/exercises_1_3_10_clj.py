from link_stack import LinkStack


def InfixToPostfix(infix):
    stack_figure = LinkStack(None, 0)
    stack_operator = LinkStack(None, 0)
    for i in infix:
        if i == ")":
            num_last = stack_figure.pop()
            expr = "%s %s %s" % (stack_figure.pop(), num_last, stack_operator.pop())
            stack_figure.push(expr)
        if i.isdigit():
            stack_figure.push(i)
        elif i in ["+", "-", "*"]:
            stack_operator.push(i)

    for i in stack_figure:
        print i


def divide_str(s):
    l = []
    last = None
    for i in s:
        if i in ['(', ')', '+', '-', '*']:
            l.append(i)
        elif i.isdigit():
            if last and last.isdigit():
                l[-1] += i
            else:
                l.append(i)
        last = i
    return l


s = "((1+(2*3))-(4+5))"
s = divide_str(s)
InfixToPostfix(s)
