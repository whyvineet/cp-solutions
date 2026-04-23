import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

n = int(input())
bosses = list(map(int, input().split()))

adj = defaultdict(list)
for employee, boss in enumerate(bosses):
    adj[boss].append(employee+2)

result = [0]*(n+1)

def dfs(node):
    count = 1
    for neigh in adj[node]:
        count += dfs(neigh)
    result[node] = count-1
    return count

dfs(1)
ans = result[1:]

print(*ans)