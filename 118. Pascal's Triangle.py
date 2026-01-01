class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)

        return triangle

''' if entire triangle is asked, use this method
    time complexity : O(n ^ 2) 
    space complexity : O(n ^ 2) - for output 
'''

######################################################################################################################################################

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            curr_val = 1  # C(i, 0)

            for j in range(1, i):
                curr_val *= (i - j + 1) 
                curr_val //= j
                row[j] = curr_val

            triangle.append(row)

        return triangle


''' if paricular row is asked, use this method
    time complexity : O(n ^ 2)
    space complexity : O(n) - we don't need output triangle if one row is asked
'''

######################################################################################################################################################

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = self.get_ncr(i, j)
            triangle.append(row)

        return triangle
    
    def get_ncr(self, n, r):
        res = 1
        for i in range(r):
            res *= (n - i)
            res //= (i + 1)
        return res

''' if paricular position is asked, use this method
    time complexity : O(n ^ 2) * O(r)
    space complexity : O(1) - we don't need output triangle if one position is asked
'''

