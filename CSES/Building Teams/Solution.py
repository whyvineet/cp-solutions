from collections import deque

def solve(n, graph):

    color = [0]*(n+1)
    for i in range(1, n+1):
        if color[i] == 0:
            q = deque()
            q.append(i)
            color[i] = 1
            while q:
                node = q.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == 0:
                        color[neighbour] = 3 - color[node]
                        q.append(neighbour)
                    elif color[neighbour]==color[node]:
                        return -1
    return color[1:]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    result = solve(n, graph)
    if result != -1:
        for i in result:
            print(i, end=" ")
    else:
        print("IMPOSSIBLE")