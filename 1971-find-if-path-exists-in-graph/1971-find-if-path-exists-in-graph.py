
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False