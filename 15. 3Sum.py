class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2): 
            if nums[i] > 0: # if no -ve's we cann't get sum as 0
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
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

