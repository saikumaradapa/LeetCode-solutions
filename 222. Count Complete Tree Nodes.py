class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        left_height = self.getHeightLeft(root)
        right_height = self.getHeightRight(root)

        if left_height == right_height:
            return 2 ** left_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def getHeightLeft(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h
    
    def getHeightRight(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
        
''' 
    time complexity : (log n) ^ 2
    space complexity : O(log n)
'''

#####################################################################################################################################################################

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        if root.left and root.right :
            return 1 + self.countNodes(root.left)+self.countNodes(root.right)            
        if root.left :
            return 1+self.countNodes(root.left)
        return 1+self.countNodes(root.right)

''' time complexity : O(n)  DFS
    space complexity : O(n)
'''

#####################################################################################################################################################################


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [root]
        while q  :
            n = len(q)
            for i in range(n) :
                node = q.pop(0)
                if node :
                    q.append(node.left)
                    q.append(node.right)
                    res += 1
        return res

''' time complexity : O(n)  BFS
    space complexity : O(n)
'''

