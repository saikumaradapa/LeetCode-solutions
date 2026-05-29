class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for num in nums:
            if num < 10:
                ans = min(ans, num)
            else:
                s = 0
                while num:
                    s += num % 10
                    num //= 10
                ans = min(ans, s)
        return ans

'''
    replace each number with its digit sum, find minimum
    time complexity : O(n * d) where d = digits per number
    space complexity : O(1)
'''
