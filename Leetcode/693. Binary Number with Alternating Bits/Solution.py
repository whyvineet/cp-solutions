# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        flag = n%2
        n //= 2
        
        while n > 0:
            f = n%2
            if f == flag:
                return False
            flag = f
            n //= 2

        return True