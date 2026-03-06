class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False
        
        for ch in s:
            if ch == '0':
                seen_zero = True
            elif seen_zero:
                return False
        
        return True

''' Loop approach
    time complexity : O(n)
    space complexity : O(1)
'''

##############################################################################################################################

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

''' pattern search since leading zeros not allowed in test cases
    time complexity : O(n)
    space complexity : O(1)
'''
