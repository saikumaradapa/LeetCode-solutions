class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # pruning
                
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])  # reuse allowed
                path.pop()
        
        backtrack(0, target)
        return res

''' backtracking approach 
    time complexity : O(2 ** target)
    space complexity : O(target) - max recursion depth
'''
