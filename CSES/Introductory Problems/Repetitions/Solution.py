s = input()
n = len(s)

result = 1
i = 1
while i < n:
    cnt = 1
    while i < n and s[i] == s[i-1]:
        cnt += 1
        i += 1
    i += 1
    result = max(result, cnt)

print(result)