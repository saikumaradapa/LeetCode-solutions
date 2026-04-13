class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        res = n 

        for i in range(n):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res

''' 
      time complexity : O(n)
      space complexity : O(1)
'''
#######################################################################################################################

class Solution:
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i, x in enumerate(nums) if x == target)

''' 
      time complexity : O(n)
      space complexity : O(1)
'''

#######################################################################################################################

class Solution:
    def getMinDistance(self, nums, target, start):
        n = len(nums)
        
        for d in range(n):
            if start - d >= 0 and nums[start - d] == target:
                return d
            if start + d < n and nums[start + d] == target:
                return d

''' 
      time complexity : O(n) # early return wrost case linear
      space complexity : O(1)
'''
