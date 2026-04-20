class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0

        # compare with first element
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                res = max(res, j)
                break

        # compare with last element
        for i in range(n):
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
                break

        return res

''' check only extremes since maximum distance occurs at boundaries
    compare first element with farthest different
    compare last element with farthest different
    time complexity : O(n)
    space complexity : O(1)
'''

##############################################################################################################

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        for i in range(n):
            for j in range(n):
                if colors[i] != colors[j]:
                    res = max(res, abs(j-i))
        return res
      
''' 
    time complexity : O(n^2)
    space complexity : O(1)
'''
