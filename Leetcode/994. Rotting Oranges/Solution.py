# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        fresh = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if fresh == 0:
            return 0

        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1