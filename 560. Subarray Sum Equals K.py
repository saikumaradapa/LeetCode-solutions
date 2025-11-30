class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  
        prefix = {0 : 1}

        count = 0
        sum = 0 
        for n in nums:
            sum += n
            rem = sum - k 
            if rem in prefix:
                count += prefix[rem]

            prefix[sum] = prefix[sum] + 1 if sum in prefix else 1
        return count   
        
''' time complexity : O(n)      
    space complexity : O(n)
'''
