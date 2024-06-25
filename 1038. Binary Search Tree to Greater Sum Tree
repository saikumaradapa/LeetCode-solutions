problem link : https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/?envType=daily-question&envId=2024-06-25

# reverse_inorder_traversal 

class Solution:

    def reverse_inorder(self, node, currSum):
        if not node: return 

        self.reverse_inorder(node.right, currSum)

        currSum[0] += node.val 
        node.val = currSum[0]

        self.reverse_inorder(node.left, currSum)



    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = [0]
        self.reverse_inorder(root, currSum)
        return root 

''' time complexity : O(n)      
    space complexity : O(h) aux space 
'''


#####################################################################################################################################################################################

# my approach 

class Solution:
    def findNodes(self, root, inorder):
        if root:
            self.findNodes(root.left, inorder)
            inorder.append(root.val)
            self.findNodes(root.right, inorder)
        
    def updateNodes(self, root, inorder):
        if root:
            self.updateNodes(root.left, inorder)
            root.val = inorder.popleft()
            self.updateNodes(root.right, inorder)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.findNodes(root, inorder)

        for i in range(len(inorder)-2, -1, -1):
            inorder[i] = inorder[i] + inorder[i+1]
        
        self.updateNodes(root, deque(inorder))

        return root

''' time complexity : O(n)        
    space complexity : O(n)
'''
