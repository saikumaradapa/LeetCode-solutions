T - O(log N) S - o(1)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val :
            if root.val > val :
                root = root.left
            else :
                root = root.right 
        return root
