class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            sorted(s1[0::2]) == sorted(s2[0::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )

#################################################################################################################################

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            {s1[0], s1[2]} == {s2[0], s2[2]} and
            {s1[1], s1[3]} == {s2[1], s2[3]}
        )

#################################################################################################################################

from collections import Counter

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            Counter(s1[0::2]) == Counter(s2[0::2]) and
            Counter(s1[1::2]) == Counter(s2[1::2])
        )


#################################################################################################################################

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_match = (
            (s1[0] == s2[0] and s1[2] == s2[2]) or
            (s1[0] == s2[2] and s1[2] == s2[0])
        )
        
        odd_match = (
            (s1[1] == s2[1] and s1[3] == s2[3]) or
            (s1[1] == s2[3] and s1[3] == s2[1])
        )
        
        return even_match and odd_match
