class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        # Initialize first row
        for c in range(n):
            dp[0][c] = matrix[0][c]

        # Fill DP table
        for r in range(1, m):
            for c in range(n):

                up = dp[r-1][c]

                left = dp[r-1][c-1] if c > 0 else float("inf")

                right = dp[r-1][c+1] if c < n-1 else float("inf")

                dp[r][c] = matrix[r][c] + min(up, left, right)

        return min(dp[m-1])