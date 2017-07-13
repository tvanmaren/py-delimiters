def delim_check(str):
    open_list = ['(', '{', '<', '[']
    close_dict = {
        ')': '(',
        ']': '[',
        '>': '<',
        '}': '{',
    }
    open_stack = []
    check_switch = True

    for i in range(len(str)):
        char = str[i]
        if i > 0 and str[i-1] == '\\':
            continue
        if check_switch == False:
            if (char == '"' and open_stack[-1]=='"') or (char == "'" and open_stack[-1]=="'"):
                open_stack.pop()
                check_switch = True
        elif (char == '"' or char == "'"):
            check_switch = False
            open_stack.append(char)
        elif char in open_list:
            open_stack.append(char)
        elif char in close_dict:
            if len(open_stack) > 0 and open_stack[-1] == close_dict[char]:
                open_stack.pop()
            else:
                return False
    if len(open_stack) > 0:
        return False

    return True

assert delim_check('()') == True
assert delim_check('{}') == True
assert delim_check('[]') == True
assert delim_check('<>') == True
assert delim_check('<') == False
assert delim_check('[') == False
assert delim_check('{') == False
assert delim_check('(') == False
assert delim_check('(())') == True
assert delim_check('{{}}') == True
assert delim_check('[[]]') == True
assert delim_check('<<>>') == True
assert delim_check('{<((<{(<This is balanced>)}>))>}') == True
assert delim_check('((())') == False
assert delim_check('{{((<<))This is out of order>>}}') == False
assert delim_check('[()]{Everything matches here}{[()()]()}') == True
assert delim_check('[(abcd)]{efg}{h[i(j)k(l)m]n(o)p}qrstuvwxyz') == True
assert delim_check('Hello World! Backslashes don\\\'t (often) pass!') == True
assert delim_check('}}{{') == False
assert delim_check('))((') == False
assert delim_check(']][[') == False
assert delim_check('>><<') == False
assert delim_check('([)too soon?]') == False
assert delim_check('{(<"[(These do not count">)}') == True
assert delim_check("{(<'[(These do not count'>)}") == True
assert delim_check('{(<"(escaped">) and again: "("}') == True
assert delim_check("{(<'(escaped'>) and again: '('}") == True
assert delim_check("""{(<"(Testing ' escapism in double quote">)}""") == True
assert delim_check("""{(<'(Testing " escapism in single quote'>)}""") == True
assert delim_check('Hello World! I\\\'m (one) (awful> test case!') == False
assert delim_check('Testing mismatch of " characters') == False
assert delim_check("Testing mismatch of ' characters") == False
