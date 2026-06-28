class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        order = []

        def dfs(node):
            # Cycle found
            if state[node] == 1:
                return False

            # Already processed
            if state[node] == 2:
                return True

            # Mark as visiting
            state[node] = 1

            # Visit neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Mark as visited
            state[node] = 2

            # Add after processing all neighbors
            order.append(node)

            return True

        # Run DFS from every node
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []

        # Reverse to get topological order
        return order[::-1]