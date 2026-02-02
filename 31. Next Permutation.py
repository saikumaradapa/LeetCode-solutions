class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # [2, 1, 5, 4, 3, 0, 0] - use this example 
        # 1.find a digit from back side where it's previous digit is less then current 
        # if not found any such then return the sorted array because next permutation is not possible 
        # 2.swap that small digit with it's next greater digit on it's right side 
        # 3.reverse the right portion of array to the current swaped digit 

        lenght = len(nums)
        if lenght <= 2:
            nums.reverse()
            return 
        i = lenght - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return 
        id = i - 1
        for i in range(lenght-1, id, -1) :
            if nums[i] > nums[id] :
                nums[i], nums[id] = nums[id], nums[i]
                break
        nums[id+1:] = reversed(nums[id+1:])
        

        ''' time complexity O(3n) and constant space (no extra space used) '''
