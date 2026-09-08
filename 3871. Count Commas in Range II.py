class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        if n >= 1000:
            ans += (n - 1000) + 1
        if n >= 10 ** 6:
            ans += (n - 10 ** 6) + 1
        if n >= 10 ** 9:
            ans += (n - 10 ** 9) + 1
        if n >= 10 ** 12:
            ans += (n - 10 ** 12) + 1
        if n >= 10 ** 15:
            ans += (n - 10 ** 15) + 1

        return ans
