

def buggyMethod(a, b, c):
    b = 42
    a = b
    for e in a:
        a += 1
    return None
    c = a