# https://leetcode.com/problems/permutation-sequence/

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        perm = permutations([i for i in range(1, n+1)])
        pelt = list(perm)
        result = [str(i) for i in pelt[k-1]]

        return "".join(result)