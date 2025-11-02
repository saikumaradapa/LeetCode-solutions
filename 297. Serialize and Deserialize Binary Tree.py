# 1. BFS - level order traversal

from collections import deque
class Codec:
    def serialize(self, root):
        if not root: return ""
        res = []
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                res.append("#")
                continue 
            res.append(str(curr.val))
            q.append(curr.left)
            q.append(curr.right)
        return " ".join(res)

    def deserialize(self, data):
        if not data: return 
        vals = data.split(" ")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while i < len(vals):
            curr = q.popleft()
            if vals[i] != "#":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if vals[i] != "#":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i += 1
        return root

''' time complexity : O(n)
    space complexity : O(n)
'''

########################################################################################################################################################################################################

# 2. DFS 

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "#"
            return f"{node.val} {dfs(node.left)} {dfs(node.right)}"
        return dfs(root)

    def deserialize(self, data):
        def dfs(vals):
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs(vals)
            node.right = dfs(vals)
            return node
        return dfs(iter(data.split()))


''' time complexity : O(n)
    space complexity : O(n)
'''
