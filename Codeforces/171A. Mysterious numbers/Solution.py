a, b = map(str, input().split())
b = b[::-1]

n, m = len(a), len(b)
length = max(n, m)

a = a.rjust(length, "0")
b = b.rjust(length, "0")

result = 0
for i in range(length):
    result = result * 10
    result = result + int(a[i]) + int(b[i])

print(result)