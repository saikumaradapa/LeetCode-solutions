class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = [False] * n
        posDiag = [False] * (2*n)
        negDiag = [False] * (2*n)

        queens = [-1] * n

        def backtrack(r):
            if r == n:
                board = []
                for i in range(n):
                    row = ["."] * n
                    row[queens[i]] = "Q"
                    board.append("".join(row))
                res.append(board)
                return

            for c in range(n):
                if cols[c] or posDiag[r+c] or negDiag[r-c+n]:
                    continue

                queens[r] = c
                cols[c] = posDiag[r+c] = negDiag[r-c+n] = True

                backtrack(r+1)

                cols[c] = posDiag[r+c] = negDiag[r-c+n] = False

        backtrack(0)
        return res

'''
Backtracking

Time Complexity: O(N!)
    Row1 → N choices
    Row2 → N-1
    Row3 → N-2
    ...
    Worst case behaves like factorial.

Space Complexity: O(N) (excluding output)
    - recursion stack = N
    - cols array = N
    - diagonals = 2N
    - queens positions = N

Optimizations:
    - Use arrays instead of sets (faster lookup)
    - Avoid storing full board during recursion
    - Store only queen column positions
    - Construct board only when a solution is found

'''

######################################################################################################################################################

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]
        colSet = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in colSet or r+c in posDiag or r-c in negDiag:
                    continue

                board[r][c] = "Q"
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0)
        return res

'''
Backtracking

Time Complexity: O(N!)
    First row → N possibilities
    Second row → N-1
    ...
    Worst case factorial search tree.

Space Complexity: O(N^2)
    - board storage = N^2
    - recursion stack = N
    - sets = O(N)

Diagonal Observation:
    Positive diagonal → r + c
    Negative diagonal → r - c
'''
