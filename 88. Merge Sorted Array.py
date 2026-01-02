class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        idx = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[idx] = nums2[j]
                j -= 1
            else:
                nums1[idx] = nums1[i]
                i -= 1
            idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            idx -= 1
            j -= 1

''' 
    time complexity : O(n + m)
    space complexity : O(1)
'''
            
            
#########################################################################################################################################################


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,m+n) :
            nums1[i] = nums2[j]
            j = j+1
        nums1 = nums1.sort()
        
''' 
    time complexity : O(n+m log n+m)
    space complexity : O(1)
'''
