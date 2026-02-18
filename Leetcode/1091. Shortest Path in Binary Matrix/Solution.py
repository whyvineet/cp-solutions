# https://leetcode.com/problems/shortest-path-in-binary-matrix/

import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        n, m = len(grid), len(grid[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 1

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        pq = []
        heapq.heappush(pq, (1, (0, 0)))

        while pq:
            distance, node = heapq.heappop(pq)
            x, y = node[0], node[1]

            for dx, dy in direction:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] > distance + 1:
                    dist[nx][ny] = distance + 1
                    heapq.heappush(pq, (dist[nx][ny], (nx, ny)))

        ans = dist[n-1][m-1]

        return ans if ans != float('inf') else -1