class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for level in range(min(m, n) // 2):
            # extract layer into a list (counter-clockwise order)
            layer = []
            r1, c1 = level, level
            r2, c2 = m - 1 - level, n - 1 - level

            # top row left to right
            for c in range(c1, c2 + 1):
                layer.append(grid[r1][c])
            # right col top+1 to bottom
            for r in range(r1 + 1, r2 + 1):
                layer.append(grid[r][c2])
            # bottom row right-1 to left
            for c in range(c2 - 1, c1 - 1, -1):
                layer.append(grid[r2][c])
            # left col bottom-1 to top+1
            for r in range(r2 - 1, r1, -1):
                layer.append(grid[r][c1])

            # rotate
            total = len(layer)
            rot = k % total

            # put back rotated layer
            idx = rot
            for c in range(c1, c2 + 1):
                grid[r1][c] = layer[idx % total]
                idx += 1
            for r in range(r1 + 1, r2 + 1):
                grid[r][c2] = layer[idx % total]
                idx += 1
            for c in range(c2 - 1, c1 - 1, -1):
                grid[r2][c] = layer[idx % total]
                idx += 1
            for r in range(r2 - 1, r1, -1):
                grid[r][c1] = layer[idx % total]
                idx += 1

        return grid

'''
    extract each layer into a flat list (clockwise traversal)
    rotate list by k % perimeter positions
    write back to grid in same order
    handles rectangular grids and large k via modulo
    time complexity : O(m * n)
    space complexity : O(m + n) per layer
'''
