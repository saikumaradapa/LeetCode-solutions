Problem Link : https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0 

        for r in range(n-2):
            for c in range(m-2):
                count += self.is_magic_sqare(r, c, grid)
        return count 
    
    def is_magic_sqare(self, r, c, grid):
        # ensure 1- 9 
        seen = set()
        for i in range(r, r+3):
            for j in range(c, c+3):
                if grid[i][j] in seen or not 0 < grid[i][j] < 10:
                    return 0
                seen.add(grid[i][j])
        
        # rows sum
        for row in range(r, r+3):
            if sum(grid[row][c:c+3]) != 15:
                return 0
        
        # col sum 
        for col in range(c, c+3):
            if grid[r][col] + grid[r+1][col] + grid[r+2][col] != 15:
                return 0
        
        # diagonals sum 
        if (
            grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or 
            grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2] != 15 
        ):
            return 0
        return 1

''' 
    time complexity : O(n * m)
    space complexity : O(1)
'''        
