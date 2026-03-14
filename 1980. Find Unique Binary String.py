class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        path = ['0'] * n

        def dfs(i):
            if i == n:
                s = "".join(path)
                return s if s not in nums else None

            path[i] = '0'
            res = dfs(i + 1)
            if res:
                return res

            path[i] = '1'
            return dfs(i + 1)

        return dfs(0)

''' backtracking
    time complexity : O(n 2^n)
    space complexity : O(n)
'''        

############################################################################################################################

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')

        return "".join(res)

''' Cantor's Diagonal Argument

    idea:
    build a new string by flipping the diagonal bits

    new[i] = flip(nums[i][i])

    this guarantees the new string differs from
    nums[i] at index i for every i

    so it cannot equal any string in nums

    time complexity : O(n)
    space complexity : O(n)
'''

