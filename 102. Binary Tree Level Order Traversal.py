class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = [root]
        while q :
            lenght = len(q)
            level = []
            for i in range(lenght) :
                n = q.pop(0)
                if n :
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level :
                result.append(level)
        return result 


''' time complexity : O(n)    BFS - considering q.pop() takes O(1) time
    space complexity : O(n/2)     - max no. of nodes in a level of BT 
'''    
