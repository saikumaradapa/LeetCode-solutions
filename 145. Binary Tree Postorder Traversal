class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, visit = [], [root], [False]
        while stack :
            curr, v = stack.pop(), visit.pop()
            if curr :
                if v :
                    res.append(curr.val)
                else :
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res
            
''' time complexity : O(n), n is number of nodes
    space complexity : O(h), h is height of tree
'''


####################################################################################################################################

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root, list) :
            if root :
                postorder(root.left, list)
                postorder(root.right, list)
                list.append(root.val)

        list = []
        postorder(root, list)
        return list
