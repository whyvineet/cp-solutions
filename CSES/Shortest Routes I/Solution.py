import heapq

def solve(n, adj):
    
    dist = [float('inf')]*(n+1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))
    
    while pq:
        weight, node = heapq.heappop(pq)
        
        if weight > dist[node]:
            continue
            
        for neighbour, w in adj[node]:
            if weight + w < dist[neighbour]:
                dist[neighbour] = weight + w
                heapq.heappush(pq, (dist[neighbour], neighbour))

    ans = [str(i) for i in dist[1:]]

    return " ".join(ans)
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[]  for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        
    print(solve(n, adj))