from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)
        
        # store indices
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        ans = float('inf')
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # check consecutive triples
            for i in range(len(indices) - 2):
                span = indices[i+2] - indices[i]
                ans = min(ans, span)
        
        return -1 if ans == float('inf') else ans * 2

''' index grouping + sliding window
    time complexity : O(n)
    space complexity : O(n)
'''        
