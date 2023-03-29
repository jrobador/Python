
"""
#                        Recursion mode:
class Solution:
    def tribonacci(self, n: int) -> int:
        if (n == 0 or n == 1):
            return n
        if (n == 2):
                return 1
        else: 
            return (self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)) 
a = Solution()
print(a.tribonacci(5))

#RECURSION INTRODUCES MORE COMPLEXITY TO THE CODE -> AFTER N > 30, TIME LIMIT EXCEDEED.
"""

#                     Closure mode (my way):

def closure():
    x0 = 0
    x1 = 1
    x2 = 1
    def trib():
        nonlocal x0,x1,x2
        x3 = x0 + x1 + x2
        x0,x1,x2 = x1,x2,x3
        return x3
    return trib

class Solution:
    def tribonacci(self, n: int)-> int:
        t = closure()
        global num
        num = 0
        if (n == 1 or n == 2):
            return 1
        for i in range (3,n+1):
            num = t()
        return num
    
"""
#                    World beating way:
class Solution:
    def tribonacci(self, n: int,memo={0:0,1:1,2:1}) -> int:
        if n in memo: return memo[n]

        memo[n] = self.tribonacci(n-1,memo)+self.tribonacci(n-2,memo)+self.tribonacci(n-3,memo)
        return memo[n]
"""