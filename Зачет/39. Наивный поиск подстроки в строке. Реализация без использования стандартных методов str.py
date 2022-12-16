def search(line, s):
    for i in range(len(line)):
        for j in range(len(s)):
            if line[i + j] != s[j]:
                break
        else:
            return True
    return False


print(search("hthththththtfndsjvnfdsnviondfsniv", "htttht"))
