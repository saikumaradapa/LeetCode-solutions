class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        col = cols - 1
        count = 0

        for row in range(rows):
            while col >= 0 and grid[row][col] < 0:
                col -= 1
            count += cols - col - 1

        return count

''' 
    time complexity : O(n + m)
    space complexity : O(1)
'''
