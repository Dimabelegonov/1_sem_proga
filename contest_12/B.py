def word_ord(s):
    res = 0
    for letter in s:
        res += ord(letter)

    return res


arr = list(map(str, input().split()))
arr = sorted(arr)
arr = sorted(arr, key=lambda x: len(x))
for i in range(len(arr)):
    arr[i] = str(word_ord(arr[i]))

print(" ".join(arr))

