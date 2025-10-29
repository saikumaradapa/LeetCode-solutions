class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = True 
        q = [root]
        res = []
        while q :
            level = []
            n = len(q)
            for i in range(n) :
                node = q.pop(0)
                if node :
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level :
                if flag :
                    res.append(level)
                else :
                    res.append(level[::-1])
            flag = not flag
        return res


''' time complexity : O(n) - considering q.pop() takes O(1)
    space complexity : O(n)
'''
