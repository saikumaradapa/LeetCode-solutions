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

''' it works for a skew tree with 10^5 nodes without overlap of idx variable 
    what if it is skew tree? the width will 1 but the index become 10^5 and a integer variable may can't holds 

    time complexity : O(n)  
    space complexity : O(n)
'''

###################################################################################################################################################################

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]  
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
                    q.append((node.left, 2*(idx-first)+1))
                    q.append((node.right, 2*(idx-first)+2))      
            if first != -1 and second != -1 :            
                res = max(res, second-first+1)
        return res

''' 
    time complexity : O(n)  - idx variable will be not exceed int range
    space complexity : O(n)
'''
