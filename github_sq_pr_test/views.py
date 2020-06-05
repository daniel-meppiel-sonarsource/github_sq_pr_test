

def buggyMethod(a, b, c):
    a = b
    for e in a:
        a++
    return None
    c = a