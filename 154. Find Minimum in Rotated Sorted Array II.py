class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                ans = min(ans, nums[m])
                l = m + 1
            elif nums[m] < nums[r]:
                ans = min(ans, nums[m])
                r = m - 1
            else:
                ans = min(ans, nums[r])
                r -= 1
        return ans

'''
    binary search comparing mid with right
    nums[m] > nums[r]: min is in right half
    nums[m] < nums[r]: min could be m, search left
    nums[m] == nums[r]: can't decide, shrink r by 1
    track ans throughout since we might skip the min
    time complexity : O(n) worst, O(log n) average
    space complexity : O(1)
'''

#######################################################################################################################

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
