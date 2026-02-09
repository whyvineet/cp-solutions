# https://leetcode.com/problems/count-dominant-indices/

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n-2, -1, -1):
            nums[i] += nums[i+1]

        count = 0
        for i in range(1, n):
            if nums[i-1]-nums[i] > nums[i]/(n-i):
                count += 1

        return count