
# time O(m*n) three times and space O(1) constant space 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row, first_col = False, False 
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    if i == 0 : first_row = True 
                    if j == 0 : first_col = True 
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,len(matrix)) :
            for j in range(1,len(matrix[0])) :
                if matrix[0][j] == 0 or matrix[i][0] == 0 :
                    matrix[i][j] = 0 
        if first_row :
            for i in range(len(matrix[0])) :
                matrix[0][i] = 0
        if first_col :
            for i in range(len(matrix)) :
                matrix[i][0] = 0 





# time complexity O(m*n) and space O(k) k- number of 0 occurances worst case m*n 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        list = []
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 and (i,j) not in list :
                    list.append((i,j))
        for i, j in list :
            for i1 in range(len(matrix)) :
                matrix[i1][j] = 0
            for j1 in range(len(matrix[0])) :
                matrix[i][j1] = 0
