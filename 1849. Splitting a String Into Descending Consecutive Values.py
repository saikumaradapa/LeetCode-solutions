class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i, prev):
            if i == n:
                return True

            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])

                if num == prev - 1:
                    if dfs(j + 1, num):
                        return True

                if num >= prev:
                    break

            return False

        first = 0
        for i in range(n - 1):
            first = first * 10 + int(s[i])
            if dfs(i + 1, first):
                return True

        return False

''' Backtracking
    Time Complexity: O(n³) worst case  
    Space Complexity: O(n) recursion depth


Explanation:

1) We try every possible first number → O(n) choices.
2) For each choice, DFS scans forward building numbers → O(n).
3) Recursion depth is at most n.

So in the worst theoretical case:
O(n) × O(n) × O(n) = O(n³)

However, due to strong pruning (num >= prev break condition),
actual runtime is much smaller in practice.

Given n ≤ 20, this easily fits within limits.
'''
