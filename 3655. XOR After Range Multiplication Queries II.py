class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = (10 ** 9) + 7 
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % mod
        
        res = 0 
        for x in nums:
            res ^= x 
        return res


''' brute force | TLE ~ 10 ^ 10
    time complexity : O(n * q)
    space complexity :O(1)
'''

####################################################################################################################

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        
        import math
        B = int(math.sqrt(n)) + 1
        
        # bucket[k][r] = list of (l, r, v) queries
        # where k <= B and l % k == r
        bucket = [[] for _ in range(B + 1)]
        
        # Process queries
        for l, r, k, v in queries:
            if k > B:
                # Large k → brute force (few elements touched)
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod
            else:
                # Small k → store query
                bucket[k].append((l, r, v))
        
        # Apply small-k queries
        for i in range(n):
            value = nums[i]
            
            for k in range(1, B + 1):
                if not bucket[k]:
                    continue
                
                remainder = i % k
                
                for l, r, v in bucket[k]:
                    if l <= i <= r and (l % k) == remainder:
                        value = (value * v) % mod
            
            nums[i] = value
        
        # Compute final XOR
        res = 0
        for num in nums:
            res ^= num
        
        return res

''' 
    If k > √n → brute force
    If k ≤ √n → bucket by k
    Final answer computed by checking each index against small k buckets

    time complexity : O((n + q) √n) | Borderline for Time Limit (TLE) in python
    space complexity :O(q)
'''

accepted - optimzed solution need revise 
