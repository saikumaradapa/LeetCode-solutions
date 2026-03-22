class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        flag = [True] * 4
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    flag[0] = False
                
                if mat[i][j] != target[j][n - 1 - i]:
                    flag[1] = False
                
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    flag[2] = False
                
                if mat[i][j] != target[n - 1 - j][i]:
                    flag[3] = False
        
        return any(flag)

''' optimal without any rotations
    time complexity : O(n ^ 2)
    space complexity : O(1)
'''        
