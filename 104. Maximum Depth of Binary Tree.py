class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root  :
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

''' time complexity : O(N)
    space complexity : O(H) - H = heigth of the tree, for balanced tree H = log(n), for skew tree H = N
'''
