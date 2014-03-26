# -*- coding: UTF-8 -*-
#b标准公式输入，非全括号表达式
from link_stack import LinkStack

def infix_to_postfix(s):
    result = ""
    stack_operator = LinkStack(None, 0)
    
    for i in s:
        if i.isdigit():
            result += " %s"%i
        elif i == ")":
            while True:
                oper = stack_operator.pop()
                if oper != "(":
                    result +=" %s"%oper
                else:
                    break
        elif i in ["+", "-", "*", "/"]:
            while True:
                if not stack_operator.isEmpty():
                    oper = stack_operator.peek()
                    if oper in ["+", "-", "*", "/"]:
                        if is_priority(oper, i):
                            result  += " %s"%stack_operator.pop()
                        else:break
                    else:break
                else:break
            stack_operator.push(i)
        elif i == "(":
            stack_operator.push(i)
    if not stack_operator.isEmpty():
        for i in stack_operator:
            result += " %s"%i
    print result
    

def is_priority(oper_1, oper_2):
    #oper_2 is more prior
    if oper_1 in ["-", "+"] and oper_2 in ["*", "/"]:
        return False
    #they are equal or oper_1 is more prior
    else:
        return True


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


s = "3+2*5-4"
s = divide_str(s)
infix_to_postfix(s)
