
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        n = len(nums)

        dp = [[-1] * (targetSum + 1) for _ in range(n)]

        def f(i, target):
            if target == 0:
                return True

            if i == 0:
                return nums[0] == target

            if dp[i][target] != -1:
                return dp[i][target]

            not_take = f(i - 1, target)

            take = False
            if nums[i] <= target:
                take = f(i - 1, target - nums[i])

            dp[i][target] = take or not_take
            return dp[i][target]

        return f(n - 1, targetSum)
