class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]  
        res = 0       
        while q :
            first, second = -1, -1
            n = len(q)
            for i in range(n) :
                node, idx = q.pop(0)
                if node :
                    if first == -1 :
                        first = idx
                    second = idx
                    q.append((node.left, 2*idx-first))
                    q.append((node.right, 2*idx+1-first))
            # print(first, second)      
            if first != -1 and second != -1 :            
                res = max(res, second-first+1)
        return res

''' it works for a skew tree with 10^5 nodes without overlap of idx variable 
    what if it is skew tree? the width will 1 but the index become 10^5 and a integer variable may can't holds 

    time complexity : O(n)  
    space complexity : O(n)
'''

##########################################################################################################################################################################################

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]  
        res = 0       
        while q :
            first, second = -1, -1
            n = len(q)
            for i in range(n) :
                node, idx = q.pop(0)
                if node :
                    if first == -1 :
                        first = idx
                    second = idx
                    q.append((node.left, 2*idx))
                    q.append((node.right, 2*idx+1))      
            if first != -1 and second != -1 :            
                res = max(res, second-first+1)
        return res

''' time complexity : O(n)
    space complexity : O(n)
'''

##########################################################################################################################################################################################

def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        width = 1  
        q = [(root,0)]
        while q :
            level  = []
            if len(q) != 0 :
                width = max(width, q[-1][1]-q[0][1]+1)

            while q :
                node, position = q.pop(0)
                if node.left :
                    level.append((node.left,position*2))
                if node.right :
                    level.append((node.right,position*2+1))
            q = level

        return width

