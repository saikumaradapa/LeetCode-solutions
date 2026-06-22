class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        for ch in text:
            freq[ch] += 1
        mini = float('inf')
        for ch in "ban":
            mini = min(mini, freq[ch])
        for ch in "lo":
            mini = min(mini, freq[ch] // 2)
        return mini

'''
    "balloon" needs b:1, a:1, n:1, l:2, o:2
    count freq of each char, min of (freq/needed) across all required chars
    l and o need 2 each so divide by 2
    time complexity : O(n)
    space complexity : O(1)
'''
