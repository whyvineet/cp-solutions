# https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x-dx, y-dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and mat[nx][ny] > mat[x][y]+1:
                    q.append((nx, ny))
                    mat[nx][ny] = mat[x][y]+1
        
        return mat