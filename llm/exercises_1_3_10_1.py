from link_stack import LinkStack

def infix_to_postfix(s):
    stack_operator = LinkStack(None, 0)
    result = ""
    flag_mutiply = 0
    mutiply_changed = False
    flag_divide = 0
    divide_changed = False
    for i in s:
        if i == ")":
            if mutiply_changed:
                flag_mutiply += 1
            if divide_changed:
                flag_divide += 1
            result += " %s"%stack_operator.pop()
            if mutiply_changed and flag_mutiply == 1:
                result += " %s"%stack_operator.pop()
                mutiply_changed = False
                flag_mutiply = 0
            if divide_changed and flag_divide == 1:
                result += " %s"%stack_operator.pop()
                divide_changed = False
                flag_divide = 0
        elif i == "(":
            if mutiply_changed:
                flag_mutiply -= 1
            if divide_changed:
                flag_divide -= 1
        elif i.isdigit():
            result += " %s"%i
            if mutiply_changed and flag_mutiply == 1:
                result += " %s"%stack_operator.pop()
                mutiply_changed = False
                flag_mutiply = 0
            if divide_changed and flag_divide == 1:
                result += " %s"%stack_operator.pop()
                divide_changed = False
                flag_divide = 0
        elif i == "*":
            stack_operator.push(i)
            flag_mutiply = 1
            mutiply_changed = True
        elif i == "/":
            stack_operator.push(i)
            flag_divide = 1
            divide_changed = True
        elif i in ["+", "-"]:
            stack_operator.push(i)
    if not stack_operator.isEmpty():
        for i in stack_operator:
            result += " %s"%i
    print result



def divide_str(s):
    l = []
    last = None
    for i in s:
        if i in ['(', ')', '+', '-', '*', '/']:
            l.append(i)
        elif i.isdigit():
            if last and last.isdigit():
                l[-1] += i
            else:
                l.append(i)
        last = i
    return l


s = "3+(2-5*4)*6/3"
s = divide_str(s)
infix_to_postfix(s)
