class TrieNode:
    def __init__(self):
        self.children = [None] * 2
    
    def containsKey(self, bit):
        return self.children[bit] != None
    
    def put(self, bit, node):
        self.children[bit] = node
    
    def get(self, bit):
        return self.children[bit]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not curr.containsKey(bit):
                curr.put(bit, TrieNode())
            curr = curr.get(bit)
    
    def getMaxXorNum(self, num):
        curr = self.root
        maxNum = 0 
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not curr:
                return -1
            if curr.containsKey(1-bit):
                maxNum = (maxNum | (1 << i))
                curr = curr.get(1-bit)
            else:
                curr = curr.get(bit)
        return maxNum

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        nums.sort()
        newQueries = [(m, x, idx) for idx, [x, m] in enumerate(queries)]
        newQueries.sort()
        answer = [-1] * len(queries)
        idx = 0
        for m, x, i in newQueries:
            while idx < len(nums) and nums[idx] <= m:
                trie.insert(nums[idx])
                idx += 1
            answer[i] = trie.getMaxXorNum(x)
        return answer

''' 
    time complexity : O(n logn + q logq + 32(n + q))
    space complexity : O(32 * n + q)
'''
