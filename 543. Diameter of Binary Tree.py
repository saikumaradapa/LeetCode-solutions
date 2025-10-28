class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root) :
            if not root :
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left+right)
            return 1+max(left, right)
        dfs(root)
        return res[0]
        
''' time complexity : O(n)    bottom-up approach
    space complexity : O(h)
'''
