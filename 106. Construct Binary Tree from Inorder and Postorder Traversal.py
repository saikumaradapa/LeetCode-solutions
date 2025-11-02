class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(postorder)

        def helper(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            in_root_idx = idx_map[root_val]
            left_size = in_root_idx - in_left
            root.left = helper(post_left, post_left+left_size-1, in_left, in_root_idx-1)
            root.right = helper(post_left+left_size, post_right-1, in_root_idx+1, in_right)
            return root

        return helper(0, n-1, 0, n-1)

''' 
    time complexity : O(n)
    space complexity : O(n)
'''
