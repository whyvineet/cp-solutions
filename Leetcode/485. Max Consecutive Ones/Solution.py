# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        curr = 0
        for num in nums:
            if num == 0:
                count = max(count, curr)
                curr = 0
            else:
                curr += 1

        return max(count, curr)