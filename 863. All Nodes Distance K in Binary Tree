class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def takeParentNodes(root, parentSet) :
            q = [root]
            while q :
                n = len(q)
                for i in range(n) :
                    node = q.pop(0)
                    if node :
                        if node.left :
                            parentSet[node.left] = node
                            q.append(node.left)
                        if node.right :
                            parentSet[node.right] = node
                            q.append(node.right)
        parentSet = dict()
        takeParentNodes(root, parentSet) 
        visited = set()

        q = [target]
        visited.add(target)
        level_count = 0
        while q :
            n = len(q)
            if k == level_count  :
                break 

            for i in range(n) :
                node = q.pop(0)
                if node.left and node.left not in visited :
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if node in parentSet and parentSet[node] not in visited :
                    q.append(parentSet[node])
                    visited.add(parentSet[node])
            level_count += 1


        res = []
        for node in q :
            res.append(node.val)
        # print(res)
        return res


''' time complexity : O(n)+O(n)
    space complexity : O(n)+O(n)+O(n)
'''
