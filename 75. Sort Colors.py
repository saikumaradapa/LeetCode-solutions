class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # dutch natonal flag problem  
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right :
            # if 0 found, swap left with mid and move one step+ both
            if nums[mid] == 0 :
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            # if 2 found, swap right with mid and move one step- for right 
            # and don't move mid (it may be 0 or 1)
            elif nums[mid] == 2 :
                nums[mid], nums[right] = nums[right], nums[mid] 
                right -= 1
            # if 1 found, just move to next 
            else:
                mid += 1

''' low - end of sorted 0's | mid - start of unsorted | right - start of sorted 2's
    time complexity : O(n) 
    space complexity : O(1) 
'''


-----------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # bucket sort method 
        n = [0, 0, 0]
        for i in nums :
            n[i] += 1
        id = 0
        for i in range(n[0]) :
            nums[id] = 0
            id += 1
        for i in range(n[1]) :
            nums[id] = 1
            id += 1
        for i in range(n[2]) :
            nums[id] = 2
            id += 1

''' 
    time complexity : O(2n) 
    space complexity : O(1) 
'''
