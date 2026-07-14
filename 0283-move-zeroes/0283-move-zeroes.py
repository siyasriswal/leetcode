class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1