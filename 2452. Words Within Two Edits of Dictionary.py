class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def is_valid(w1, w2):
            diff = 0
            for a, b in zip(w1, w2):
                if a != b:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        res = []

        for w1 in queries:
            for w2 in dictionary:
                if is_valid(w1, w2):
                    res.append(w1)
                    break

        return res

''' compare each query with dictionary words and count mismatches
    break early if mismatches exceed 2
    append query if any dictionary word matches within 2 edits
    time complexity : O(q * d * n)
    space complexity : O(1)
'''
