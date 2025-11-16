Problem Link : https://leetcode.com/problems/making-a-large-island/description/


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n 
    
    def findParent(self, node):
        if self.parent[node] == node:
            return node 
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        
        if ulp_u == ulp_v:
            return False 
        
        if self.size[ulp_u] <= self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v 
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u 
            self.size[ulp_u] += self.size[ulp_v]
            
        self.count -= 1
        return True 

class Solution:
    def getPosition(self, row, col, cols):
        return row * cols + col
    
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols    
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = DisjointSet(n * m)
        visited = [[0] * m for _ in range(n)]
        
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
        one_count = 0 
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    one_count += 1
                    current_position = self.getPosition(row, col, m)
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if self.isValid(new_row, new_col, n, m) and grid[new_row][new_col]:
                            adjacent_position = self.getPosition(new_row, new_col, m)
                            ds.unionBySize(current_position, adjacent_position)
        if one_count == n * m:
            return n * m
        if one_count == 0:
            return 1
            
        res = -1
        for row in range(n):
            for col in range(m):
                parent_set = set()
                if grid[row][col] == 0:
                    current_position = self.getPosition(row, col, m)
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if self.isValid(new_row, new_col, n, m) and grid[new_row][new_col]:
                            adjacent_position = self.getPosition(new_row, new_col, m)
                            parent_set.add(ds.findParent(adjacent_position))
                
                res = max(sum([ds.size[node] for node in parent_set]) + 1, res)
        return res

''' time complexity : O(n * m * 4 * alpha)
    space complexity : O(n * m)
'''
