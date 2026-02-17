import heapq

def solve(n, adj):
    
    dist = [float('inf')]*(n+1)
    dist[1] = 0
    parent = [-1]*(n+1)
    
    pq = []
    heapq.heappush(pq, (0, 1))
    
    while pq:
        weight, node = heapq.heappop(pq)
        
        if weight > dist[node]:
            continue
            
        for neighbour, w in adj[node]:
            if weight + w < dist[neighbour]:
                dist[neighbour] = weight + w
                parent[neighbour] = node
                heapq.heappush(pq, (dist[neighbour], neighbour))
    
    ans = []
    i = n
    while parent[i] != -1:
        ans.append(str(i))
        i = parent[i]

    if ans:
        result = " ".join(reversed(ans))
        result = "1 " + result
        return result
    
    return -1
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[]  for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    print(solve(n, adj))