# https://cses.fi/problemset/task/1667/

from collections import deque

def solve(n, adj):
    q = deque()
    visited = [False] * (n + 1)
    path = [-1] * (n + 1)

    q.append(1)
    visited[1] = True

    while q:
        node = q.popleft()

        for neighbour in adj[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                path[neighbour] = node
                q.append(neighbour)

    return path

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    path = solve(n, adj)

    if path[n] == -1:
        print("IMPOSSIBLE")
    else:
        result = []
        cur = n

        while cur != -1:
            result.append(cur)
            cur = path[cur]

        result.reverse()

        print(len(result))
        print(*result)
