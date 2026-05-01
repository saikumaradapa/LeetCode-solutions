class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        res = f
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            res = max(res, f)
        return res

'''
    F(k) = F(k-1) + sum(nums) - n * nums[n-k]
    compute F(0) directly, then derive each next in O(1)
    time complexity : O(n)
    space complexity : O(1)
'''
