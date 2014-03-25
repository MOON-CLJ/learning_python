from link_stack import LinkStack

def insert_parentheses(s):
    stack_figure = LinkStack(None, 0)
    stack_operator = LinkStack(None, 0)
    for i in s:
        if i == ")":
            num_last = stack_figure.pop()
            expr = " ( %s %s %s )" %(stack_figure.pop(), stack_operator.pop(), num_last)
            stack_figure.push(expr)
        elif i.isdigit():
            stack_figure.push(i)
        elif i == " ":
            pass
        else:
            stack_operator.push(i)
    for i in stack_figure:
        print i


s = "1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )"
insert_parentheses(s)

