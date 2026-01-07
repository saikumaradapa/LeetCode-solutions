# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum_tree(root)
        max_product = [-1]
        self.get_max_product(root, root.val, max_product)
        return max_product[0] % 1000000007
    def sum_tree(self, root):
        if not root:
            return 0
        left = self.sum_tree(root.left)
        right = self.sum_tree(root.right)
        root.val = root.val + left + right 
        return root.val 
    def get_max_product(self, root, total_sum, max_product):
        if root.left:
            max_product[0] = max(max_product[0], (total_sum - root.left.val) * root.left.val)
            self.get_max_product(root.left, total_sum, max_product)
        if root.right:
            max_product[0] = max(max_product[0], (total_sum - root.right.val) * root.right.val)
            self.get_max_product(root.right, total_sum, max_product)
