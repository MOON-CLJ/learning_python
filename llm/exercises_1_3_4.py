from link_stack import LinkStack

def parentheses(s):
    stack = LinkStack(None, 0)
    for i in s:
        if i == "(":
            stack.push(")")
        elif i == "[":
            stack.push("]")
        elif i == "{":
            stack.push("}")
        else:
            if stack.isEmpty() or i != stack.pop():
                print "False"
                return
    print "True"

                 
s = ["[", "(", ")", "]"]
parentheses(s)
