def find_root(f, a, b, tol):
    if abs(a - b) < tol:
        pass
    m = (a + b) / 2
    y = f(m)
    if abs(y) < 10 ** -6 and abs(a - b) < tol:
        return m
    else:
        if y < 0:
            return find_root(f, m, b, tol)
        else:
            return find_root(f, a, m, tol)

