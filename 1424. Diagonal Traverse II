class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(nums)) :
            for j in range(len(nums[i])) :
                res.append((i+j, j, nums[i][j]))
        res.sort()
        return [t[2] for t in res]



''' time complexity : O(n log(n))
    space complexity : O(n) 
'''

################################################################################################################################################################
TLE

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        maxColumn = 0
        n = len(nums)
        for row in range(n) :
            maxColumn = max(maxColumn,len(nums[row]))
        maxIndex = max(n, maxColumn)

        for i in range(maxIndex-n) :
            nums.append([0] * (maxIndex))

        for row in nums :
            if len(row) < maxIndex :
                row += [0] * (maxIndex-len(row))
        n = len(nums)
        for i in range(n) :
            j = 0
            while i >= 0 and j < len(nums[i]) :
                if nums[i][j] != 0 :
                    res.append(nums[i][j])
                i -= 1
                j += 1
        for j in range(1, len(nums[-1])) :
            i = len(nums[-1])-1
            while i >= 0 and j < len(nums[i]) :
                if nums[i][j] != 0 :
                    res.append(nums[i][j])
                i -= 1
                j += 1
        return res




''' time complexity : O(m*n)
    space complexity : O(m*n) for result
'''
