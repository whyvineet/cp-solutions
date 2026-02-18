# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        result = list(s)

        for i in range(len(indices)):
            result[indices[i]] = s[i]

        return "".join(result)