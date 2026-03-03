class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

''' standard backtracking In-Place Swapping
    time complexity : O(n!)
    space complexity : O(1)
'''

#########################################################################################################

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack()
                
                path.pop()
                used[i] = False

        backtrack()
        return res
        
''' standard backtracking with visited array
    time complexity : O(n!)
    space complexity : O(n)
'''

#########################################################################################################

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # if the len of list is 1 return it as list
        # for i in entire len of list  
        # take remove first element then find permutations of that list then 
        # append the removed element at end of permutations 
        # entend the permutations to result list
        # again add removed element to nums


        if len(nums) == 1 :
            return [nums[:]]
        for i in range(len(nums)) :
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms :
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

''' element elimination method | neetcode
    time complexity : O(n * n!)
    space complexity : O(1)
'''
