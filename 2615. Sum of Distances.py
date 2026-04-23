from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = defaultdict(list)

        # group indices
        for i, v in enumerate(nums):
            index_map[v].append(i)

        res = [0] * len(nums)

        for indices in index_map.values():
            prefix = [0]
            for idx in indices:
                prefix.append(prefix[-1] + idx)

            m = len(indices)

            for pos, idx in enumerate(indices):
                # left side
                left = pos * idx - prefix[pos]

                # right side
                right = (prefix[m] - prefix[pos + 1]) - (m - pos - 1) * idx

                res[idx] = left + right

        return res


''' group indices of same values and use prefix sums to compute distances
    left = pos * idx - sum_left
    right = sum_right - count_right * idx
    avoids binary search by processing in order
    time complexity : O(n)
    space complexity : O(n)
'''
