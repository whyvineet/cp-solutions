from collections import defaultdict, deque

n = int(input())

adj = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    dist = [-1]*(n+1)
    q = deque([start])
    dist[start] = 0
    
    while q:
        node = q.popleft()
        for neigh in adj[node]:
            if dist[neigh] == -1:
                dist[neigh] = dist[node] + 1
                q.append(neigh)
    
    return dist, node

dist1, end1 = bfs(1)
dist2, end2 = bfs(end1)
dist3, end3 = bfs(end2)

result = [0]*n
for i in range(1, n+1):
    result[i-1] = max(dist1[i], dist2[i], dist3[i])

print(*result)