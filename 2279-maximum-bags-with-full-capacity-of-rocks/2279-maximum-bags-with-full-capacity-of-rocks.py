class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need=[]
        count=0
        for c, r in zip(capacity, rocks):
            need.append(c-r)
        need.sort()
        for x in need:
            if x<=additionalRocks:
                additionalRocks-=x
                count +=1
            else:
                break
        return count