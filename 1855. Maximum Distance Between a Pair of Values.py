class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        i, j = 0, 0 

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
                j = max(j, i)

        return res

''' use two pointers leveraging non-increasing property to greedily expand j and adjust i
    time complexity : O(n + m)
    space complexity : O(1)
'''

##########################################################################

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        for i in range(len(nums1)):
            l, r = i, len(nums2) - 1
            j = -1

            while l <= r:
                m = (l + r) // 2
                if nums1[i] <= nums2[m]:
                    j = m
                    l = m + 1
                else:
                    r = m - 1

            if j != -1:
                res = max(res, j - i)

        return res

''' for each index in nums1, binary search farthest valid j in nums2
    time complexity : O(n log m)
    space complexity : O(1)
'''
