class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        perm = []
        used = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue

                used[i] = True
                perm.append(nums[i])

                backtrack()

                perm.pop()
                used[i] = False

        backtrack()
        return res

''' Sorting + Skip Duplicates with backtracking
    time complexity : O(n * n!)
    space complexity : O(n)
'''


#####################################################################################################################



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {n : 0 for n in nums}
        res = []
        perm = []
        for i in nums :
            count[i] += 1
        def backtrack() :
            if len(perm) == len(nums) :
                res.append(perm[:])
                return 
            for i in count :
                if count[i] != 0:
                    count[i] -= 1
                    perm.append(i)
                    backtrack()
                    count[i] += 1
                    perm.pop()
          
        backtrack()
        return res
        
        
''' frequency map + backtracking
    time complexity : O(n * n!)
    space complexity : O(n + k)
'''
