class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n

        def func(index):

            if index == 0:
                return nums[0]

            if index < 0:
                return 0

            if dp[index] != -1:
                return dp[index]

            pick = nums[index] + func(index - 2)
            notpick = func(index - 1)

            dp[index] = max(pick, notpick)

            return dp[index]

        return func(n - 1)