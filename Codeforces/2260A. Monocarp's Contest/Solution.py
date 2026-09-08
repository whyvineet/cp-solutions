def solve(n, arr):
    easy = 0
    for i in range(n):
        easy += 1 if arr[i] == 0 else 0

    if arr[0] == 0 and arr[n-1] == 0:
        return 0
    if easy <= 1:
        return -1

    return 1 if arr[0] == 0 or arr[n-1] == 0 else 2

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(result)