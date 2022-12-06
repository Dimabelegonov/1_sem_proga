def is_add_35(n):
    if n == 1:
        return True
    if n < 0:
        return False
    if n > 0:
        return is_add_35(n - 5) or is_add_35(n - 3)

