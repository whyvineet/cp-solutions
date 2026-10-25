n = int(input())

result = [-1] * n

for i in range(n - (1 + n % 2), -1, -2):
    result[i] = (i + 1) // 2

for i in range(0, n, 2):
    result[i] = (n + i) // 2 + 1

check = False
for i in range(1, n):
    if abs(result[i] - result[i-1]) == 1:
        check = True
        break

if check:
    print('NO SOLUTION')
else:
    print(*result)