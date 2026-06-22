class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses

        def dfs(node):

            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True