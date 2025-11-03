class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root 
        stack = []
        n = 0
        while stack or curr :
            while curr :
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k :
                return curr.val 
            curr = curr.right 
                
''' Iterative solution 
    time complexity : O(n)                
    space complexity : O(n) 
'''

#########################################################################################################################################################################################

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count, result):
            if node:
                count, result = dfs(node.left, count, result)
                count += 1
                if count == k:
                    result = node.val
                    return count, result
                count, result = dfs(node.right, count, result)
            return count, result
        
        count, result = dfs(root, 0, None)
        return result

                
''' time complexity : O(n)                
    space complexity : O(n) for recursive stack 
'''

#########################################################################################################################################################################################

# Brute force approch 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []
        def inorder(root,list) :
            if root :
                inorder(root.left,list)
                list.append(root.val)
                inorder(root.right, list)
        inorder(root, list)
        return list[k-1]

''' time complexity : O(n)                
    space complexity : O(n)
'''
