class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        res = float('inf')
        
        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                res = min(res, diff, n - diff)
        
        return res if res != float('inf') else -1

'''
    time complexity : O(n)
    space complexity : O(1)
'''
