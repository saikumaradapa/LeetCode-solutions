class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] != float('-inf') and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[n-1] if dp[n-1] != float('-inf') else -1

'''
    dp[i] = max jumps to reach index i from index 0
    for each i, check all j < i where jump is valid (diff <= target)
    only update from reachable states (dp[j] != -inf)
    time complexity : O(n^2)
    space complexity : O(n)
'''
