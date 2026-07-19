class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def func(r,c):
            
            if r==0 and c==0:
                return grid[0][0]
            if r<0 or c<0:
                return float("inf")

            if dp[r][c] != -1:
                return dp[r][c]
            up=func(r-1,c)
            left=func(r,c-1)
            dp[r][c]=grid[r][c]+min(up,left)

            return dp[r][c] 
        return func(m-1,n-1)
