# https://leetcode.com/problems/redundant-connection/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.component = n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pv] = pu
            self.size[pv] += self.size[pu]
        self.component -= 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = [max(u, v) for u, v in edges]
        dsu = DSU(max(n)+1)

        ans = [-1, -1]
        for u, v in edges:
            if not dsu.union(u, v):
                ans = [u, v]

        return ans