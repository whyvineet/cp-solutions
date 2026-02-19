# https://leetcode.com/problems/bus-routes/

from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0
        
        n = len(routes)
        graph = defaultdict(list)

        for i in range(n):
            for stop in routes[i]:
                graph[stop].append(i)

        visited = set()
        q = deque()

        for route in graph[source]:
            q.append((route, 1))
            visited.add(route)

        while q:
            node, change = q.popleft()

            if target in routes[node]:
                return change

            for stop in routes[node]:
                for neighbour in graph[stop]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour, change+1))

        return -1