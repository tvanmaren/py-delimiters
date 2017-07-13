def delim_check(str):
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
    for char in str:
        if char in open_list:
            delim_vals[char] += 1
            last_open.append(char)
        elif char in close_dict:
            if last_open.pop() == close_dict[char]:
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
assert delim_check('{<((<{(<>)}>))>}') == True
assert delim_check('((())') == False
assert delim_check('{{((<<))>>}}') == False
