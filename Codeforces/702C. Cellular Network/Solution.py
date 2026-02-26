# https://codeforces.com/problemset/problem/702/C

from bisect import bisect_left

def solve(n, m, cities, towers):
    towers.sort()
    ans = 0

    for city in cities:
        idx = bisect_left(towers, city)

        min_dist = float('inf')

        if idx < m:
            min_dist = min(min_dist, abs(towers[idx] - city))

        if idx > 0:
            min_dist = min(min_dist, abs(towers[idx - 1] - city))

        ans = max(ans, min_dist)

    return ans


n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

print(solve(n, m, cities, towers))