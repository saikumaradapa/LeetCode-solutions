# Iterative solution 

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root : return TreeNode(val)
        curr = root 
        while True :
            if curr.val < val :
                if curr.right :
                    curr = curr.right 
                else :
                    curr.right = TreeNode(val)
                    break 
            else :
                if curr.left :
                    curr = curr.left 
                else :
                    curr.left = TreeNode(val)
                    break 
        return root

''' time complexity : O(logn)
    space complexity : O(1)
'''

##############################################################################################################################################################################################################################


# Recursive solution

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return TreeNode(val)
        if root.val < val :
            if root.right :
                self.insertIntoBST(root.right, val)
            else :
                root.right = TreeNode(val)
        else :
            if root.left :
                self.insertIntoBST(root.left, val)
            else :
                root.left = TreeNode(val)
        return root
    
''' time complextiy : O(logn)
    space complextiy : O(n)   - auxiliary space for recursive stack 
'''
