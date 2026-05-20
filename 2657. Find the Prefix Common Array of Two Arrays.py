class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        C = [0] * n
        curr = 0
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                curr += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                curr += 1
            C[i] = curr
        return C

'''
    single freq array: increment for both A[i] and B[i]
    when freq hits 2, that number appeared in both → increment count
    works because each number appears exactly once in each permutation
    time complexity : O(n)
    space complexity : O(n)
'''


###############################################################################################################

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        f1, f2 = defaultdict(int), defaultdict(int)
        C = [0] * len(A)
        curr = 0
        for i in range(len(A)):
            f1[A[i]] += 1
            f2[B[i]] += 1
            if A[i] == B[i]:
                curr += 1
                C[i] = curr
                continue
            if f1[A[i]] == 1 and f2[A[i]] != 0:
                curr += 1
            if f2[B[i]] == 1 and f1[B[i]] != 0:
                curr += 1
            C[i] = curr
        return C

'''
    track freq of A and B separately
    when A[i] == B[i], both become common at once
    otherwise check if A[i] was already in B (f2), and if B[i] was already in A (f1)
    curr = running count of common elements
    time complexity : O(n)
    space complexity : O(n)
'''
