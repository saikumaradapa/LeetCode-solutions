# Most Optimal Approach

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

''' Morris Traversal Pattern
    time complexity : O(n)
    space complexity : O(1)
'''

##########################################################################################################################################################

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if not root: return None 

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None 

            last = rightTail or leftTail or root
            return last 
        
        dfs(root)
        # return root 

''' time complexity : O(n)
    space complexity : O(h)
'''

##########################################################################################################################################################

# Bruteforce Approach 

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root, arr) :
            if not root :
                return 
            arr.append(root)
            left, right = root.left, root.right 
            root.left, root.right = None, None
            dfs(left, arr)
            dfs(right, arr)
        arr = []
        dfs(root, arr)
        for idx in range(len(arr)-1) :
            arr[idx].right = arr[idx+1]


''' time complexity : O(n)
    space complexity : O(h)
'''

