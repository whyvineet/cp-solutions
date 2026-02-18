# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = grid[0][0]

        direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        pq = []
        heapq.heappush(pq, (0, (0, 0)))

        while pq:
            weight, position = heapq.heappop(pq)
            x, y = position[0], position[1]

            if weight > dist[x][y]:
                continue

            for dx, dy in direction:
                nx, ny = x+dx, y+dy

                if 0 <= nx < n and 0 <= ny < m and weight + grid[x][y] < dist[nx][ny]:
                    dist[nx][ny] = weight + grid[x][y]
                    heapq.heappush(pq, (dist[nx][ny], (nx, ny)))

        print(dist)

        return dist[n-1][m-1]