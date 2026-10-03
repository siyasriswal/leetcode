class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        l=0
        for num in seen:
            if num-1 not in seen:
                current = num
                count = 1
                while current +1 in seen:
                    current +=1
                    count +=1
                l=max(l,count)
        return l


       