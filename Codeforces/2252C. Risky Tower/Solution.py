def solve(n, m, v, grid):
    result = m
    curr = []
    for i in range(n-1, -1, -1):
        curr.extend(grid[i])
        curr.sort(reverse=True)
        curr = curr[:m]
        stab = 0
        for j in range(m):
            stab += curr[j]
            if stab >= v[i]:
                result = min(result, j+1)
                break

    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

    result = solve(n, m, v, grid)
    print(result)