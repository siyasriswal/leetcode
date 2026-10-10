class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i=m-1
        j=n-1
        dp = [[-1] * n for _ in range(m)]
        def f(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            up=f(i-1,j)
            left=f(i,j-1)
            dp[i][j]= up+left
            return dp[i][j]
        return f(i,j)
