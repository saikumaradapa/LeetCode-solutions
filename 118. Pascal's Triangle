import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows) :
            temp = []
            for j in range(i+1) :
                temp.append(math.comb(i,j))
            result.append(temp)
        return result
        
        



class Solution:
    def generate(self, n: int) -> List[List[int]]:
        result = []
        for i in range(n) :
            temp = []
            for j in range(i+1) :
                if j ==0 or j == i :
                    temp.append(1)
                else :
                    temp.append(result[i-1][j]+result[i-1][j-1])
            result.append(temp)

        return result
