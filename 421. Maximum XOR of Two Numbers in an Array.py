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
            if curr.containsKey(1-bit):
                maxNum = (maxNum | (1 << i))
                curr = curr.get(1-bit)
            else:
                curr = curr.get(bit)
        return maxNum


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for num in nums:
            trie.insert(num)
        
        maxNum = 0
        for num in nums:
            maxNum = max(maxNum, trie.getMaxXorNum(num))
        return maxNum

''' 
    time complexity : O(32 * n)
    space complexity : O(32 * n)
'''
