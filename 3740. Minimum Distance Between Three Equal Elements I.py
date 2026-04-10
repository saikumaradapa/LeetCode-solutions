class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break
        return -1 if ans == n + 1 else ans * 2
      
''' brute force
    time complexity : O(n^3)
    space complexity : O(1)
'''      

####################################################################################################################

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
