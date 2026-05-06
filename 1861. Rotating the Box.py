class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])
        newGrid = [[''] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                newGrid[j][n-i-1] = boxGrid[i][j]

        for c in range(n):
            r = m - 1
            for l in range(m-1, -1, -1):
                if newGrid[l][c] == "#":
                    newGrid[l][c], newGrid[r][c] = newGrid[r][c], newGrid[l][c]
                    r -= 1
                elif newGrid[l][c] == "*":
                    r = l - 1

        return newGrid

'''
    step 1: rotate 90 degrees clockwise → newGrid[j][n-i-1] = boxGrid[i][j]
    step 2: apply gravity per column — stones fall to lowest empty spot
    r = next available position (bottom up)
    stone: swap to r, move r up
    obstacle: reset r to just above obstacle
    time complexity : O(n * m)
    space complexity : O(n * m) for the new grid
'''
