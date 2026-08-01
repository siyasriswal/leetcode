class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float("inf")
        maxi=0
        for price in prices:
            mini=min(mini,price)
            profit=price-mini
            maxi=max(maxi,profit)
        return maxi