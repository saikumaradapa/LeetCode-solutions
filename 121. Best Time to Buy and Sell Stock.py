class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # take maximum profit and minimum cost 
        
        maxp, minv =0, max(prices)
        for i in prices :
            minv = min(i , minv) 
            maxp = max(i-minv , maxp)
        return maxp

''' we are memorizing that the reason tag as Dynamic Programming
    time complexity : O(n)
    space complexity : O(1)
'''
