class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        nums.sort()
        left = 0
        max_len = 0
        
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_len = max(max_len, right - left + 1)
        
        return n - max_len

''' sliding window
    time complexity : O(n logn)
    space complexity : O(1)
'''
