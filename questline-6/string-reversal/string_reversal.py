def reverse_iterative(s):
    result = ""
    index = len(s) - 1
    while index >= 0:
        result += s[index]
        index -= 1
    return result

def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

