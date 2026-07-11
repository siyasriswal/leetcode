class Solution:
    def findPeakElement(self, num: List[int]) -> int:
        l=0
        r=len(num)-1
        while l<r:
            mid=(l+r)//2
            if num[mid]>num[mid+1]:
                r=mid
            else:
                l=mid+1
        return l
    
            