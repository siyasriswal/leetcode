class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        a = [0] * len(nums)
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                a[j] = nums[i]
                j += 1

        nums[:] = a