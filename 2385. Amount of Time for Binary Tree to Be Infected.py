class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root: return 0
        parents = dict()
        self.getParents(root, parents)
        target_node = self.getNode(root, start)
        q = deque([(target_node, 0)])
        res = 0
        visited = set()
        while q:
            curr, t = q.popleft()
            res = t 
            if curr in visited:
                continue 
            visited.add(curr)
            if curr.left and curr.left not in visited:
                q.append((curr.left, t + 1))
            if curr.right and curr.right not in visited:
                q.append((curr.right, t + 1))
            if curr in parents and parents[curr] not in visited:
                q.append((parents[curr], t + 1))
        
        return res
                
    def getParents(self, root, parents):
        if not root: return 
        if root.left:
            parents[root.left] = root
            self.getParents(root.left, parents)
        if root.right:
            parents[root.right] = root
            self.getParents(root.right, parents)
        
    def getNode(self, root, target):
        if root:
            if root.val == target:
                return root
            return self.getNode(root.left, target) or self.getNode(root.right, target)
        
        
''' 
    time complexity : O(3n)
    space complexity : O(3n)
'''
