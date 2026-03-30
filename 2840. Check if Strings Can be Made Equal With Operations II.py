class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (
            sorted(s1[0::2]) == sorted(s2[0::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )

'''
    time complexity : O(n log n)
    space complexity : O(n)
'''

#########################################################################################################################################################

from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (
            Counter(s1[0::2]) == Counter(s2[0::2]) and
            Counter(s1[1::2]) == Counter(s2[1::2])
        )

'''
    Since characters are only lowercase English letters (26 letters), We can use frequency counting instead of sorting.
    time complexity : O(n)
    space complexity : O(1)
'''

#########################################################################################################################################################

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0]*26
        odd = [0]*26
        
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            
            if i % 2 == 0:
                even[idx1] += 1
                even[idx2] -= 1
            else:
                odd[idx1] += 1
                odd[idx2] -= 1
        
        return all(x == 0 for x in even) and all(x == 0 for x in odd)


'''
    single pass true linear solution
    time complexity : O(n)
    space complexity : O(1)
'''
