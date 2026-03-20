class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        ans = [[0] * (COLS - k + 1) for _ in range(ROWS - k + 1)]

        for row in range(0, ROWS - k + 1):
            for col in range(0, COLS - k + 1):
                window = []
                for r in range(row, row + k):
                    for c in range(col, col + k):
                        window.append(grid[r][c])
                window.sort()
                curr_abs_min = float('inf')
                for i in range(1, len(window)):
                    if window[i-1] != window[i]:
                        curr_abs_min = min(curr_abs_min, window[i] - window[i-1])
                ans[row][col] = curr_abs_min if curr_abs_min != float('inf') else 0
        return ans

''' simulation
    time complexity : O((ROWS-k+1) * (COLS-k+1) * (k^2 + k^2 logk^2 + k^2))
    space complexity : O(k^2)
'''
