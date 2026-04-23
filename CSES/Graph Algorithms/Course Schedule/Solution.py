from collections import deque

def solve(n, edges):
    adj = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    visited = set()

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        node = q.popleft()
        visited.add(node)
        ans.append(node)

        for neighbour in adj[node]:
            if neighbour not in visited:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

    for i in indegree:
        if i != 0:
            return None

    return ans
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edge = map(int, input().split())
        edges.append(edge)
    result = solve(n, edges)
    if result is None:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=" ")