def word_ord(s):
    res = 0
    for letter in s:
        res += ord(letter)

    return res


def long(s):
    return len(s) >= 5


arr = list(filter(long, input().split()))
for i in range(len(arr)):
    arr[i] = str(word_ord(arr[i]))

print(" ".join(arr))
