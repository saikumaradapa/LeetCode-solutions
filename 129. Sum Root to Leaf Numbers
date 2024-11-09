Problem Link : https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, curr) :
            nonlocal res        
            if not root : return 

            curr += str(root.val)
            if not root.left and not root.right : 
                res += int(curr)
                return 
            
            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root, "")    
        return res
    
''' time complexity : O(n)         DFS
    space complexity : O(1)
'''

######################################################################################################################################################

from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,str(root.val))])
        res = 0
        while q:
            node, curr = q.popleft()
            if not node.left and not node.right:
                res += int(curr)
            
            if node.left:
                q.append((node.left, curr+str(node.left.val)))
            
            if node.right:
                q.append((node.right, curr+str(node.right.val)))
            
        return res

''' time complexity : O(n)           BFS 
    space complexity : O(n)
'''
