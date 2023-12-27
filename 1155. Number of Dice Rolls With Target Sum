class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        cache = {}
        def count(n, target) :
            if n == 0 :
                return 1 if target == 0 else 0
            if (n, target) in cache :
                return cache[(n, target)]                
            res = 0
            for val in range(1, k+1) :
                res = (res + count(n-1, target-val)) % mod 
            cache[(n, target)] = res
            return res
        return count(n, target)

''' time complexity : O(n*k*target)        
    space complexity : : O(n*k)
'''

########################################################################################################################################################################################################


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        def count(n, target) :
            if n == 0 :
                return 1 if target == 0 else 0
            res = 0
            for val in range(1, k+1) :
                res = (res + count(n-1, target-val)) % mod 
            return res
        return count(n, target)

''' time complexity : O(k^n)        
    space complexity : : O(n)
'''
