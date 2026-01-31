class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        # Ensure nums1 is smaller
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        total = n1 + n2
        half = (total + 1) // 2
        is_even = (total % 2 == 0)

        l, r = 0, n1

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = half - mid1

            left1  = nums1[mid1-1] if mid1 > 0 else float('-inf')
            right1 = nums1[mid1]   if mid1 < n1 else float('inf')
            left2  = nums2[mid2-1] if mid2 > 0 else float('-inf')
            right2 = nums2[mid2]   if mid2 < n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if is_even:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1, left2)

            elif left2 > right1:
                l = mid1 + 1
            else:
                r = mid1 - 1

''' optimal approach | binary search
    time complexity : O(log(min(n, m)))
    space complexity : O(1)
'''

#######################################################################################################################################################

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
        
        n = len(nums1) + len(nums2)
        return nums3[n//2]  if n % 2 != 0 else (nums3[n//2] + nums3[(n//2)-1])/2

''' better approach 
    time complexity : O(m + n)
    space complexity : O(n)
'''

#######################################################################################################################################################

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1+nums2)
        return nums1[len(nums1)//2] if len(nums1)%2 != 0 else (nums1[len(nums1)//2-1]+nums1[len(nums1)//2])/2

''' brute force approach 
    time complexity : O(n logn)
    space complexity : O(n)
'''
