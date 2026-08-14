class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0 
        freq = defaultdict(int)
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

''' 
    time complexity : O(n)
    space complexity : O(26) - at max 26 characters
    sliding window approach
'''
