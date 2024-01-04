class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        def dfs(root) :
            if not root :
                return 0
            
            left = max(0,dfs(root.left))            
            right = max(0,dfs(root.right))
            total = root.val+left+right 
            res[0] = max(res[0], total)
            return root.val + max(left, right)
        dfs(root)
        return res[0]

''' time complexity : O(n)        dfs - bottom up approach 
    space compleixty : O(h)
'''        
