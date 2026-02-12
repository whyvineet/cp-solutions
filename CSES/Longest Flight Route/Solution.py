from collections import deque

def solve(n, edges):
    
    adj = [[] for _ in range(n+1)]
    visited = set()
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
        visited.add(node)

        for neighbour in adj[node]:
            if neighbour not in visited:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
    
    dp = [float('-inf')] * (n+1)
    dp[1] = 0
    parent = [-1] * (n+1)

    for node in topo:
        for nxt in adj[node]:
            if dp[node] + 1 > dp[nxt]:
                dp[nxt] = dp[node] + 1
                parent[nxt] = node


    if dp[n] < 0:
        return 0, "IMPOSSIBLE"

    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    if path[0] != 1:
        return 0, "IMPOSSIBLE"

    return dp[n] + 1, " ".join(map(str, path))


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    result, path = solve(n, edges)
    if result == 0:
        print(path)
    else:
        print(result)
        print(path)