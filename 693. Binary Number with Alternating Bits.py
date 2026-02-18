class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0

''' XOR Bit Trick
    time complexity : O(1)
    space complexity : O(1)
'''

###############################################################################################################################################################################

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        expected = n & 1  # last bit
    
        n >>= 1
        
        while n:
            if (n & 1) == expected:
                return False
            expected = n & 1
            n >>= 1
        
        return True

''' Iterative Bit Checking
    time complexity : O(logn)
    space complexity : O(1)
'''
