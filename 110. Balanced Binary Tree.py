class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node) :
            if not node :
                return (0, True)
            
            left_height, left_balanced = helper(node.left)
            right_height, right_balanced = helper(node.right)

            return (max(left_height, right_height)+1, left_balanced and right_balanced and abs(left_height-right_height) <= 1 )

        return helper(root)[1]

''' time complexity : O(n)  
    space complexity : O(h)
  '''
