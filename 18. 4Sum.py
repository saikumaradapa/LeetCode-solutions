class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n) :
            if i > 0 and nums[i] == nums[i-1] :
                continue 
            for j in range(i+1, n) :
                if j != i+1 and nums[j-1] == nums[j] :
                    continue 
                t = target-nums[i]-nums[j]
                left, right = j+1, n-1
                while left < right :
                    if nums[left]+nums[right] > t :
                        right -= 1
                    elif nums[left]+nums[right] < t :
                        left += 1
                    else :
                        res.append([nums[i], nums[j], nums[left], nums[right]]) 
                        while left < right and nums[left] == nums[left+1] :
                            left += 1
                        while left < right and nums[right] == nums[right-1] :
                            right -= 1
                        left += 1
                        right -= 1
        return res
        
''' 
    time complexity O(n ^ 3) - two pointer approach
    space complexity O(1)  
'''


########################################################################################################################################################


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        n = len(nums)

        def kSum(k, start, t) :
            if k != 2 :
                for i in range(start, n-k+1) :
                    if i > start and nums[i] == nums[i-1] :
                        continue                    
                    quad.append(nums[i])
                    kSum(k-1, i+1, t-nums[i]) 
                    quad.pop()
                return 


            left, right = start, n-1
            while left < right :
                if nums[left]+nums[right] > t :
                    right -= 1
                elif nums[left]+nums[right] < t :
                    left += 1
                else :
                    res.append(quad+[nums[left],nums[right]])
                    left += 1
                    # right -= 1
                    while left<right and nums[left] == nums[left-1] :
                        left += 1
                    while left<right and nums[right] == nums[right-1] :
                        right -= 1                        
                            
        kSum(4, 0, target)
        return res


''' 
    time complexity O(k - 1) - ksum solution
    space complexity O(n)  
'''

########################################################################################################################################################


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in seen:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        res.add(tuple(temp[:]))
                    seen.add(nums[k])
        return list(res)


''' 
    time complexity O(n ^ 3) - taken set operations as constant 
    space complexity O(n)  
'''
