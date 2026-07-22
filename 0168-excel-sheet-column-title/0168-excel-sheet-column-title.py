class Solution:
   
    def convertToTitle(self, columnNumber: int) -> str:
        mapit={}
        index=1
        for i in range(65,91):
            mapit[index]=chr(i)
            index+=1
      
        ans=""
        while columnNumber:
            if columnNumber%26!=0:
                ans+=mapit[columnNumber%26]
                columnNumber-=(columnNumber%26)
            else:
                ans+=mapit[26]
                columnNumber-=26

            columnNumber//=26
        return ans[::-1]