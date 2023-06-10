# * one line solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        return [[i,len(nums)-nums[::-1].index(target-nums[i])-1] for i in range(len(nums)) if target-nums[i] in nums[i+1:]][0]

# 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(len(nums)) :
            if target- nums[i] in nums[i+1:] :
                return [i, n-nums[::-1].index(target-nums[i])-1]
            



# 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums[:]
        nums = sorted(nums)

        left, right = 0, len(nums)-1
        while left < right  :
            if nums[left]+nums[right] == target :
                return [nums2.index(nums[left]), len(nums2)-1-nums2[::-1].index(nums[right])]

            elif nums[left]+nums[right] > target :
                right -= 1
            else :
                left += 1





# 3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}
        for i in range(len(nums)) :
            complement = target-nums[i]
            if complement in dit :
                return [dit[complement], i]
            else :
                dit[nums[i]] = i




# 4 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)) :
                if nums[i]+nums[j] == target :
                    return list((i,j))



