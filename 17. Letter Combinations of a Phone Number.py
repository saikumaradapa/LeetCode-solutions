class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        path = []
        n = len(digits)

        def dfs(i):
            if i == n:
                res.append("".join(path))
                return

            for ch in phone[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res

''' backtracking
    time complexity : O(n * 4^n)
    space complexity : O(n) - auxilary space 
'''        
