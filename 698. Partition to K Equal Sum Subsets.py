class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)
        used = [False] * n

        if nums[0] > target:
            return False

        def dfs(i, k, curr_sum):
            if k == 1:
                return True
            # k == 1 ? If you have successfully formed k-1 subsets correctly,
            # the remaining unused elements must automatically sum to target.

            if curr_sum == target:
                return dfs(0, k-1, 0)

            for j in range(i, n):
                if used[j] or curr_sum + nums[j] > target:
                    continue

                used[j] = True
                if dfs(j+1, k, curr_sum + nums[j]):
                    return True
                used[j] = False

                # symmetry pruning
                if curr_sum == 0:
                    break

            return False

        return dfs(0, k, 0)

''' backtracking
    time complexity : O(k 2 ^ n)
    space complexity : O(n)
'''
