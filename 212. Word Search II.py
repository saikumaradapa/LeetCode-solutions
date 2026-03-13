class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word here
      
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # store word at end
        
        rows, cols = len(board), len(board[0])
        res = []
        
        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            ch = board[r][c]
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            
            # Found word
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicates
            
            board[r][c] = "#"  # mark visited
            
            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)
            
            board[r][c] = ch  # restore
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return res

'''

The improved version just removes extra bookkeeping.

| Improvement            | Benefit           |
| ---------------------- | ----------------- |
| Remove visited matrix  | Less memory       |
| Store word in trie     | No join cost      |
| Less parameter passing | Cleaner recursion |
| No currWord list       | Simpler state     |

bookkeeping means : Keeping track of extra information needed to make an algorithm work.
It usually refers to auxiliary variables, structures, or steps used to maintain state.
'''



#########################################


class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res = set()
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, currNode, currStr):
            if (i < 0 or j < 0 or 
                i == ROWS or j == COLS or 
                (i, j) in visit or board[i][j] not in currNode.child):
                return 
            
            visit.add((i, j))
            currNode = currNode.child[board[i][j]]
            currStr += board[i][j]

            if currNode.isWord:
                res.add(currStr)
            

            dfs(i-1, j, currNode, currStr)
            dfs(i, j-1, currNode, currStr)
            dfs(i+1, j, currNode, currStr)
            dfs(i, j+1, currNode, currStr)

            visit.remove((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in root.child:
                    dfs(i, j, root, "")
        return list(res)

''' Trie + Backtracking + Pruning
    time complexity : O(WL + m*n*4^L)
    space complexity : O(WL)
'''
