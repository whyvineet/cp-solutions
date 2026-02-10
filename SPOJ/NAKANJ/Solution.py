# https://www.spoj.com/problems/NAKANJ/

from collections import deque

move = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

def solve(x1, y1, x2, y2):

    dir = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    visited = set()

    q = deque()
    q.append((x1, y1))

    dist = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            if x == x2 and y == y2:
                return dist
            for cx, cy in dir:
                nx, ny = x+cx, y+cy
                if nx >= 1 and nx < 9 and ny >= 1 and ny < 9 and (nx, ny) not in visited:
                    q.append((nx, ny))
        dist += 1
    
    return dist

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(str, input().split())

        x1, y1 = move[a[0]], int(a[1])
        x2, y2 = move[b[0]], int(b[1])

        result = solve(x1, y1, x2, y2)
        print(result)