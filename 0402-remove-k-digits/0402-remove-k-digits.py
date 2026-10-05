class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # 1. Process all digits to maintain a monotonic stack
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # 2. OUTSIDE THE FOR LOOP: Handle leftover removals
        # [:-k] drops the last k elements (the largest remaining digits)
        if k > 0:
            stack = stack[:-k]
            
        # 3. Format result and strip leading zeros
        r = "".join(stack)
        cl = r.lstrip("0")
        
        if len(cl) == 0:
            return "0"
        else:
            return cl