class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    
    dsu = DSU(n)
    for i in range(1, n+1):
        dsu.union(i, lst[i-1])
    
    result = [0]*n
    for i in range(1, n+1):
        par = dsu.find(i)
        result[i-1] = dsu.size[par]

    print(*result)
