def solve(n, arr):

    midx = arr.index(min(arr))
    xidx = arr.index(max(arr))

    left = max(midx, xidx) + 1
    right = n - min(midx, xidx)
    both = min(midx, xidx) + (n - max(midx, xidx)) + 1

    return min(left, right, both)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))