''' Moore’s Voting Algorithm '''
''' time complexity O(n)
    space complexity O(1) '''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None
        n = len(nums)
        for i in range(n) :
            if count == 0 :
                element = nums[i]
                count  = 1
            elif nums[i] == element :
                count += 1
            else :
                count -= 1
        return element

        # count1 = 0
        # for i in range(n) :
        #     if nums[i] == element :
        #         count1 += 1
        # if count1 > n//2 :
        #     return element 
        # return -1



----------------------------------------------------------------------------------------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums) :
            if nums.count(i)  > len(nums)//2 :
                return i
                
                
----------------------------------------------------------------------------------------------------------------                
                
                
                
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        nums.sort()
        return nums [int (size/2)]
