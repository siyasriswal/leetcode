class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        totalSum = sum(stones)
        target = totalSum // 2
        n = len(stones)

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        if stones[0] <= target:
            dp[0][stones[0]] = True
        for i in range(1, n):
            for t in range(1, target + 1):
                not_take = dp[i - 1][t]
                take = False
                if stones[i] <= t:
                    take = dp[i - 1][t - stones[i]]
                dp[i][t] = take or not_take
        for s in range(target, -1, -1):
            if dp[n - 1][s]:
                return totalSum - 2 * s
        return 0