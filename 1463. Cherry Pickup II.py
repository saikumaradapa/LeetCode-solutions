class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Base case: last row
        prev = [[0] * COLS for _ in range(COLS)]
        for j1 in range(COLS):
            for j2 in range(COLS):
                prev[j1][j2] = grid[ROWS - 1][j1]
                if j1 != j2:
                    prev[j1][j2] += grid[ROWS - 1][j2]

        # Build from bottom to top
        for i in range(ROWS - 2, -1, -1):
            curr = [[0] * COLS for _ in range(COLS)]

            for j1 in range(COLS):
                for j2 in range(COLS):

                    best = float('-inf')

                    for dj1 in (-1, 0, 1):
                        for dj2 in (-1, 0, 1):
                            nj1, nj2 = j1 + dj1, j2 + dj2

                            if 0 <= nj1 < COLS and 0 <= nj2 < COLS:
                                best = max(best, prev[nj1][nj2])

                    cherries = grid[i][j1]
                    if j1 != j2:
                        cherries += grid[i][j2]

                    curr[j1][j2] = cherries + best

            prev = curr

        return prev[0][COLS - 1]

'''
    time complexity : O(rows * cols² * 9)
    space complexity : O(cols²)
'''
