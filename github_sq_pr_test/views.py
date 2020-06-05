

def buggyMethod(a, b, c):
    a = b
    for e in a:
        a += 1
    return None
    c = a