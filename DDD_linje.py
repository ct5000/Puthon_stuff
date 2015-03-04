def punkt_linje(a, x, b, y):
    line = a * x + b
    if line == y:
        return "LINJE"
    elif line < y:
        return "OVER"
    else:
        return "UNDER"

