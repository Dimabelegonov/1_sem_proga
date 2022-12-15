def func(a, b):
    if len(a) != len(b):
        return False
    else:
        for cha, chb in zip(a, b):
            if cha != chb:
                return False
        return True


print(func(input(), input()))
