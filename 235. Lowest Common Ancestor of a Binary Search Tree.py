class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root 
        while root :
            if p.val < curr.val and q.val < curr.val :
                curr = curr.left 
            elif p.val > curr.val and q.val > curr.val :
                curr = curr.right 
            else :
                return curr 

''' time complexity : O(logn)
    space complexity : O(1)
'''
