class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

'''
    subarrays can overlap and repeat
    the largest possible value of any subarray = max(nums) - min(nums)
    pick that subarray k times
    time complexity : O(n)
    space complexity : O(1)
'''
