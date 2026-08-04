class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lo, hi = min(nums), max(nums)
        present = [False] * (hi - lo + 1)
        for x in nums:
            present[x - lo] = True
        return [i + lo for i in range(len(present)) if not present[i]]

"""
    time complexity : O(n + range), where range = hi - lo + 1
    space complexity : O(range) for the boolean array

    Boolean direct-address table: allocate a flat array covering [lo, hi],
    mark each num as present, then collect unmarked indices.
    Avoids hashing overhead of a set — constant factor is smaller.
"""
