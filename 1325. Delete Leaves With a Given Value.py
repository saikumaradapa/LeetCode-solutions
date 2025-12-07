class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        
        if root.val == target and not root.left and not root.right:
            return None
        return root 


''' time complexity : O(n)        post order approach with recursion
    space complexity : O(n)
'''


##############################################################################################################################################################################################



class Solution:
    def findLeafsAndParents(self, root, target):
        q = deque([root])
        parent_map = dict()
        leafs = []
        while q:
            node = q.popleft()
            if node.left:
                parent_map[node.left] = node 
                q.append(node.left)
            if node.right:
                parent_map[node.right] = node 
                q.append(node.right)
            
            if not node.left and not node.right and node.val == target:
                leafs.append(node)
        return leafs, parent_map


    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        leafs, parent_map = self.findLeafsAndParents(root, target)
        q = deque(leafs)

        while q:
            node = q.popleft()

            if root == node:
                return 

            parent = parent_map[node]         
            
            if parent.left == node:
                parent.left = None 
            if parent.right == node:
                parent.right = None 

            if not parent.left and not parent.right and parent.val == target:
                q.append(parent)
            

        return root

''' time complexity : O(n)        my own approach with recursion
    space complexity : O(n)
'''
