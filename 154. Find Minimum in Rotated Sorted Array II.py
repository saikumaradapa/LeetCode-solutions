class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[high] : 
                high = high -1
            elif nums[mid] > nums[high]:  
                    low = mid + 1
            else:  
                high = mid
        return nums[low]

''' time complexity : O(longn)-best    O(n)-worst 
    space complexity : O(1)
'''
