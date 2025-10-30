class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left, right = root.left, root.right
        def is_same(left, right) :
            if not left or not right :
                return left==right

            return left.val == right.val and is_same(left.left, right.right) and is_same(left.right, right.left)

        return is_same(left,right)

'''
    time complexity : O(n)
    space complexity : O(h)
'''
