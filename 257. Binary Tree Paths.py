class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root : return []
        q = [(root, '')]
        
        while q :
            n = len(q)
            for i in range(n) :
                curr,s = q.pop(0)
                s = s+'->'+str(curr.val) if s else str(curr.val)
                if not curr.left and not curr.right :
                    res.append(s)
                if curr.left :
                    q.append((curr.left, s))
                if curr.right :
                    q.append((curr.right, s))
        return res

'''
Time Complexity:
    O(N * L)
    - N is number of nodes.
    - L is the average length of the path string, which in the worst case is O(N) (for a skewed tree).
    - For each node, string concatenation and copying can cost up to O(L).
    - In total, building all path strings and collecting all leaf paths results in O(N^2) worst-case if every path is maximal length.

Space Complexity:
    O(N * L)
    - res[] list stores up to O(N) strings, each of length up to O(L) (worst case: O(N) deep tree).
    - The queue also requires O(N) space in the worst case.
    - Total space: O(N^2) in the worst case if each string is O(N) long.
'''
