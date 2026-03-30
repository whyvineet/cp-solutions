s = input()

q = a = res = 0
for i in s:
    if i == 'Q':
        res += a
        q += 1
    elif i == 'A':
        a += q

print(res)