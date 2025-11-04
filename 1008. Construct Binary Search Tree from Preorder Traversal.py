# use bound property 

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(bound, idx, n):
            if idx[0] == n or preorder[idx[0]] > bound:
                return 
            root = TreeNode(preorder[idx[0]])
            idx[0] += 1
            root.left = helper(root.val, idx, n)
            root.right = helper(bound, idx, n)
            return root
        return helper(float("inf"), [0], len(preorder))

''' time complexity : O(n)                
    space complexity : O(h)
'''

####################################################################################################################################################################################

# Construct Binary Search Tree from Preorder and inorder traversal (sort preorder to get inorder)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def insert(root, val) :
            if root.val < val :
                if root.right :
                    insert(root.right, val)
                else :
                    root.right = TreeNode(val)
            elif root.val > val :
                if root.left :
                    insert(root.left, val)
                else :
                    root.left = TreeNode(val)
            return root 
        for val in preorder[1:] :
            insert(root, val)
        return root


''' time complexity : O(n logn) - n ^ 2 for skew tree
    space complexity : O(n) - for auxiliary space
'''

####################################################################################################################################################################################

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        n = len(preorder)
        root = TreeNode(preorder[0])
        stack.append(root)

        for i in range(1, n) :
            # if the value is less than the nodes val then take current value as left 
            if preorder[i] < stack[-1].val :
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            # if the value is grater than the nodes val then take current value as right for the parent node  
            else :
                while stack and preorder[i] > stack[-1].val  :
                    last = stack.pop()
                last.right = TreeNode(preorder[i])
                stack.append(last.right)

        return root 

''' time complexity : O(n)                
    space complexity : O(n) 
'''
