# Recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)

        result = []
        inorder(root, result)
        return result

# Time complexity: O(n)
# Space complexity: O(n) (recursive call stack)

############################################################################################################################################

# Iteration 1
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

# Time complexity: O(n)
# Space complexity: O(h), where h is the height of the tree (in the worst case, h = n for a skewed tree)

############################################################################################################################################

# Iteration 2
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if stack:
                    node = stack.pop()
                    res.append(node.val)
                    curr = node.right
                else:
                    break
        return res

# Time complexity: O(n)
# Space complexity: O(h), where h is the height of the tree (in the worst case, h = n for a skewed tree)
