class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                ans += cost[i]
        return ans

'''
    greedy: sort descending, buy 2 most expensive, get 3rd free
    every 3rd candy (index 2, 5, 8...) is free
    time complexity : O(n log n)
    space complexity : O(1)
'''
