# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        count = 0
        for i in range(left, right+1):
            binary = bin(i)
            c = binary.count('1')
            if self.isPrime(c):
                count += 1

        return count

    def isPrime(self, num):
        if num <= 1:
            return False
        
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False

        return True