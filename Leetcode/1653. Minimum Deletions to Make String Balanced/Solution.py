# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n = len(s)

        countB = [0]*n
        for i in range(1, n):
            if s[i-1] == 'b':
                countB[i] = 1 + countB[i-1]
            else:
                countB[i] = countB[i-1]

        countA = [0]*n
        for i in range(n-2, -1, -1):
            if s[i+1] == 'a':
                countA[i] = 1 + countA[i+1]
            else:
                countA[i] = countA[i+1]
        
        result = float('inf')
        for i in range(n):
            result = min(result, countA[i]+countB[i])

        return result