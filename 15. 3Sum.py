class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(len(nums)-1) :
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            left, right = i+1, n-1
            target = -nums[i]
            while left < right :
                if nums[left]+nums[right] > target:
                    right -= 1
                elif nums[left]+nums[right] < target:
                    left += 1
                else :
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1] :
                        left += 1
                    while left < right and nums[right] == nums[right-1] :
                        right -= 1
                    left += 1
                    right -= 1
        return res



''' 
    time complexity O(n ^ 2) 
    space complexity O(1)  
'''



########################################################################################################################################################


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if target in seen:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                seen.add(nums[j])
                
        return list(res)

''' 
    time complexity O(n ^ 2) 
    space complexity O(n)  
'''

