def matryoshka(n):
    if n == 1:
        print("matryoshechka")
        return
    print(f"verh matryoshki {n}")
    matryoshka(n - 1)
    print(f"niz matryoshki {n}")

