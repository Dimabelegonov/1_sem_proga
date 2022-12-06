s = input()

answer = ""
for i in range(len(s)):
    answer += f"{s[i]}*10^{len(s) - i - 1} + "


print(answer[:-3])
