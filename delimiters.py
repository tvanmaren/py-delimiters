def delim_check(str):
    check_switch = True
    delim_vals = {
        '(': 0,
        '{': 0,
        '[': 0,
        '<': 0,
    }
    close_dict = {
        ')': '(',
        ']': '[',
        '>': '<',
        '}': '{',
    }
    open_list = ['(', '{', '<', '[']
    last_open = []
    for i in range(len(str)):
        char = str[i]
        if i > 0 and str[i-1] == '\\':
            continue
        if check_switch == False:
            if (char == '"' and last_open[-1]=='"') or (char == "'" and last_open[-1]=="'"):
                last_open.pop()
                check_switch = True
            continue
        elif (char == '"' or char == "'"):
            check_switch = False
            last_open.append(char)
            continue
        if char in open_list:
            delim_vals[char] += 1
            last_open.append(char)
        elif char in close_dict:
            if len(last_open) > 0 and last_open.pop() == close_dict[char]:
                delim_vals[close_dict[char]] -= 1
            else:
                return False
    for key, val in delim_vals.items():
        if val != 0:
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
assert delim_check('{<((<{(<>)}>))>}') == True
assert delim_check('((())') == False
assert delim_check('{{((<<))>>}}') == False
assert delim_check('[()]{}{[()()]()}') == True
assert delim_check('[(abcd)]{efg}{h[i(j)k(l)m]n(o)p}qrstuvwxyz') == True
assert delim_check('Hello World! I\'m (not) really here!') == True
assert delim_check('}}{{') == False
assert delim_check('))((') == False
assert delim_check(']][[') == False
assert delim_check('>><<') == False
assert delim_check('([)]') == False
assert delim_check('{(<"This is a test[(">)}') == True
assert delim_check('{(<"[(This is a test">)}') == True
assert delim_check('{(<"(This is a test">) and again: "("}') == True
assert delim_check("{(<'(This is a test'>) and again: '('}") == True
assert delim_check("""{(<"(This is a test of ' escapism">)}""") == True
assert delim_check("""{(<'(This is a test of " escapism'>)}""") == True
assert delim_check('Hello World! I\\\'m (one) (awful> test case!') == False
assert delim_check('Testing mismatch of " characters') == False
