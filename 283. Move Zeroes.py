
# optimal solution [two pointers with swap]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

''' time complexity : O(n)        
    space complexity : O(1)
'''

#########################################################################################################################################################


# TLE brute force approach  [bubble sort approach moving zeros to end one by one]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)) :
            for j in range(len(nums)-i-1) :
                if nums[j]==0 :
                    nums[j],nums[j+1] = nums[j+1], nums[j]

''' time complexity : O(n)        
    space complexity : O(1)
'''

#########################################################################################################################################################
# optimal solution [two pointers with shifting non-zeros to starting]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i in range(len(nums)) :
            if nums[i] != 0:
                nums[position]= nums[i]
                position +=1 
            
        while position < len(nums) :
            nums[position]= 0
            position += 1


''' time complexity : O(n)        
    space complexity : O(1)
'''
