class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=1
        maxx=""
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                count +=1
            else:
                count =1
            if count >=3:
                maxx=max(maxx,num[i])   
        if maxx=="":
            return ""
        return maxx*3 