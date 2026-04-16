from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        index = defaultdict(list)
        n = len(nums)

        # build index map
        for i, val in enumerate(nums):
            index[val].append(i)

        res = []

        for q in queries:
            val = nums[q]
            arr = index[val]

            # if only one occurrence
            if len(arr) == 1:
                res.append(-1)
                continue

            # find position of q in arr
            pos = bisect.bisect_left(arr, q)

            # neighbors (circular)
            left = arr[pos - 1] if pos > 0 else arr[-1]
            right = arr[pos + 1] if pos < len(arr) - 1 else arr[0]

            # compute circular distances
            d1 = abs(q - left)
            d2 = abs(q - right)

            res.append(min(d1, n - d1, d2, n - d2))


''' n = len(nums), m = len(queries)
    time complexity : O(n + m logn)
    space complexity : O(n + m)
'''
        return res
