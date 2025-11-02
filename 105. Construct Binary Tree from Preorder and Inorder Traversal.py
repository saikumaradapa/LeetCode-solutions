class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(preorder)

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root_idx = idx_map[root_val]
            left_size = in_root_idx - in_left
            root.left = helper(pre_left+1, pre_left+left_size, in_left, in_root_idx-1)
            root.right = helper(pre_left+left_size+1, pre_right, in_root_idx+1, in_right)
            return root

        return helper(0, n-1, 0, n-1)

''' 
    time complexity : O(n)
    space complexity : O(n)
'''
