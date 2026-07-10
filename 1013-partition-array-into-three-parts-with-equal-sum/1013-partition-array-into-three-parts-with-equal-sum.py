class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3 != 0:
            return False
        target=total//3
        cur=0
        c=0
        for num in arr:
            cur += num
            if cur== target:
                c+=1
                cur=0
                if c >= 3:
                    return True
        return False
      