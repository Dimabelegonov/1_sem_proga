def get_weight(s):
    data = {"C": 12, "H": 1, "N": 14, "O": 16}
    i = 0
    ans = 0
    while i < len(s):
        if i + 1 < len(s):
            if s[i + 1].isdigit():
                ans += int(s[i + 1]) * data[s[i]]
                i += 2
            else:
                ans += data[s[i]]
                i += 1
        else:
            ans += data[s[i]]
            i += 1

    return ans


def merge_by_molweight(L, R):
    ans = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if get_weight(L[i]) <= get_weight(R[j]):
            ans.append(L[i])
            i += 1
        else:
            ans.append(R[j])
            j += 1

    if i == len(L):
        for h in range(j, len(R)):
            ans.append(R[h])
    else:
        for h in range(i, len(L)):
            ans.append(L[h])

    return ans

