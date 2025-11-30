class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n, m = len(matrix), len(matrix[0])

        left, right, top, bottom = 0, m - 1, 0, n - 1
        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            if left <= right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
        
''' 
    Time complexity O(m*n)
    Space complexity O(m*n) - to store the result list 
'''
