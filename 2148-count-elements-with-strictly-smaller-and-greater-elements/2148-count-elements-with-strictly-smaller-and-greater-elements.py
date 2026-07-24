class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        count = 0

        for num in nums:
            if smallest < num < largest:
                count += 1

        return count