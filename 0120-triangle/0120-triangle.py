class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)

        dp = [[0] * len(row) for row in triangle]

        # Base case
        for j in range(len(triangle[n - 1])):
            dp[n - 1][j] = triangle[n - 1][j]

        # Bottom-up
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):

                down = dp[i + 1][j]
                diagonal = dp[i + 1][j + 1]

                dp[i][j] = triangle[i][j] + min(down, diagonal)

        return dp[0][0]