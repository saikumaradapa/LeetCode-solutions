class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s, start=1):
            print((i, ch))
            ans += (26 - (ord(ch) - ord("a"))) * i
        return ans
