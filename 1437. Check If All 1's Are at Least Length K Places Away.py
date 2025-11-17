class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_idx = float("inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_one_idx != float("inf") and i - prev_one_idx <= k:
                    return False 
                prev_one_idx = i 
        return True

''' time complexity : O(n)
    space complexity : O(1)
'''
