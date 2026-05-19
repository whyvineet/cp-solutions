n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [[0] * n for _ in range(2)]
result[1][0] = c
for i in range(1, n):
    stairs, lift = a[i-1], b[i-1]
    
    ltl = lift
    stl = lift + c

    result[0][i] = min(result[0][i-1] + stairs, result[1][i-1] + stairs)
    result[1][i] = min(result[1][i-1] + ltl, result[0][i-1] + stl)

answer = [0] * n
for i in range(n):
    answer[i] = min(result[0][i], result[1][i])

print(*answer)