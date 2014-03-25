from link_stack import LinkStack
from link_queue import LinkQueue

def infix_to_postfix(s):
    s_new = format_s(s)
    queue_figure = LinkQueue(None, None, 0)
    stack_operator = LinkStack(None, 0)
    result = ""
    for i in s_new:
        if i == ")":
            queue_figure.enqueue(stack_operator.pop())
        elif i == "(" or i == " ":
            pass
        elif i.isdigit():
            queue_figure.enqueue(i)
        else:
            stack_operator.push(i)
    
    for i in queue_figure:
        result += " %s"%i
    print result


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


s = "((1 + 122) * 23)"
infix_to_postfix(s)
