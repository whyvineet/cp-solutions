from collections import deque

global MOD
MOD = 10**9 + 7

def solve(n, edges):
    
    adj = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.append(neighbour)
    
    dp = [0] * (n+1)
    dp[1] = 1

    for node in topo:
        for neighbour in adj[node]:
            dp[neighbour] = (dp[neighbour] + dp[node]) % MOD

    return dp[n] % MOD


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    result = solve(n, edges)
    print(result)