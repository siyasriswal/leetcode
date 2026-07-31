class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        ans=[]
        for candy in candies:
            ans.append(candy + extraCandies >= maxi)

        return ans