class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=[]
        for i in range(len(nums)):
            if val!=nums[i]:
                k.append(nums[i])
            for i in range(len(k)):
                nums[i] = k[i]

        return len(k)