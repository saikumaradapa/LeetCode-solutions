class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_product = 1
        suffix_product = 1
        max_product = max(nums)

        for i in range(n):
            if prefix_product == 0:
                prefix_product = 1
            if suffix_product == 0:
                suffix_product = 1
            
            prefix_product *= nums[i]
            suffix_product *= nums[n - i - 1]

            max_product = max(max_product, prefix_product, suffix_product)
        return max_product


''' solution came from observations, odd -ve's, even -ve's, 0's
    time complexity : O(n)
    space complexity : O(1)
'''

#########################################################################################################################################################

# TLE 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = min(nums)
        for i in range(n) :
            pt = 1
            for j in range(i,n) :
                pt *= nums[j]
                res = max(res, pt)
        return res

''' time complexity : O(n ^ 2)
    space complexity : O(1) 
'''
