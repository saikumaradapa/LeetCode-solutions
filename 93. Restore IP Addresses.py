class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        n = len(s)

        def dfs(i):
            if len(path) == 4:
                if i == n:
                    res.append(".".join(path))
                return

            remaining_digits = n - i
            remaining_segments = 4 - len(path)

            if remaining_digits < remaining_segments or remaining_digits > remaining_segments * 3:
                return

            for j in range(i, min(i+3, n)):
                segment = s[i:j+1]

                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

                path.append(segment)
                dfs(j+1)
                path.pop()

        dfs(0)
        return res

''' backtracking 
    time complexity : O(3 ^ 4)
    space complexity : O(1)
'''

