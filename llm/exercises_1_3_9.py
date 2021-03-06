from link_stack import LinkStack

def insert_parentheses(s):
    s_new = format_s(s)
    stack_figure = LinkStack(None, 0)
    stack_operator = LinkStack(None, 0)
    for i in s_new:
        if i == ")":
            num_last = stack_figure.pop()
            str = " ( %s %s %s ) " %(stack_figure.pop(), stack_operator.pop(), num_last)
            stack_figure.push(str)
        elif i.isdigit():
            stack_figure.push(i)
        elif i == " ":
            pass
        else:
            stack_operator.push(i)
    for i in stack_figure:
        print i


def format_s(s):
    s_new = []
    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit():
            while s[i+1].isdigit():
                char += "%s"%(s[i+1])
                i += 1
        s_new.append(char)
        i += 1
    return s_new


s = "1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )"

insert_parentheses(s)

