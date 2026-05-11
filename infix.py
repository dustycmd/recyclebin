def priority(op):
    if op == '^': return 3
    if op in '*/': return 2
    if op in '+-': return 1
    return 0

def infix_to_postfix(expr):
    stack, res = [], ""
    for c in expr:
        if c.isalnum(): 
            res += c
        elif c == '(': 
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(': 
                res += stack.pop()
            stack.pop() # Remove '('
        else:
            while stack and priority(stack[-1]) >= priority(c):
                res += stack.pop()
            stack.append(c)
    
    while stack: res += stack.pop()
    return res

def infix_to_prefix(expr):

    rev = ""
    for c in expr[::-1]:
        if c == '(': rev += ')'
        elif c == ')': rev += '('
        else: rev += c

    return infix_to_postfix(rev)[::-1]


inf = "(A+B)*(C-D)"
print("Postfix:", infix_to_postfix(inf))
print("Prefix:", infix_to_prefix(inf))
