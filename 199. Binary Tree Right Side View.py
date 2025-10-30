class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]
        while q :
            level = None
            n = len(q)
            for i in range(n) :
                node = q.pop(0)
                if node :
                    level = node.val
                    q.append(node.left)
                    q.append(node.right)
            if level != None:
                res.append(level)
        return res


''' time complexity : O(n)
    space complextiy : O(n)
'''
