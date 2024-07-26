Problem Link : https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=daily-question&envId=2024-07-26

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf')] * n for _ in range(n)]

        for u, v, w in edges:
            matrix[u][v] = w 
            matrix[v][u] = w 
        
        for i in range(n):
            matrix[i][i] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])
        

        resLen = float('inf')
        res = -1

        for i in range(n):
            curr = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    curr += 1
            
            if curr <= resLen:
                resLen = curr
                res = i 
        

        return res
