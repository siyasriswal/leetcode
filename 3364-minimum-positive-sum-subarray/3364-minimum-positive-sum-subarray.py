class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for size in range(l, r + 1):

            # First window
            window_sum = sum(nums[:size])

            if window_sum > 0:
                ans = min(ans, window_sum)

            # Slide the window
            for right in range(size, n):
                window_sum += nums[right]
                window_sum -= nums[right - size]

                if window_sum > 0:
                    ans = min(ans, window_sum)

        return ans if ans != float('inf') else -1