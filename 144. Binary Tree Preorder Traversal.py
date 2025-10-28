class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root 
        while curr or stack :
            while curr :
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return res
        
''' iterative solution
    time complexity : O(n)
    space complexity : O(n) 
'''

################################################################################################################################################
# recursion solution 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       def preorder(root,result) :
           if  root :
                result.append(root.val)
                preorder(root.left,result)
                preorder(root.right,result)
       result = []
       preorder(root,result)
       return result
