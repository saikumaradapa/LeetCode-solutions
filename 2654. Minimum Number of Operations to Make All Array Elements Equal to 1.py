class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = 0
        cur_gcd = 0
        for n in nums:
            if n == 1:
                one_count += 1
            cur_gcd = self.gcd(cur_gcd, n)
        if one_count != 0:
            return len(nums) - one_count
        if cur_gcd != 1:
            return -1
        
        min_sub_len = float("inf")
        for l in range(len(nums)):
            cur_gcd = 0
            for r in range(l, len(nums)):
                if r - l + 1 > min_sub_len:
                    break 
                cur_gcd = gcd(cur_gcd, nums[r])
                if cur_gcd == 1:
                    min_sub_len = r - l + 1
                    break 
        return (min_sub_len -1) + len(nums) - 1

    
    def gcd(self, a, b):
        while a and b:
            a = a % b
            b, a = a, b
        return max(a, b)

''' hints
    1. we need atleast one 1 in the nums
    2. gcd operation is associative 
    time complexity : O(n^2 logm) - log m is for calculating gcd
    space complexity : O(1)
'''
