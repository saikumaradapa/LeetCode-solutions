class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        total = 0
        for i in range(k):
            gain = happiness[i] - i
            if gain <= 0:
                break
            total += gain

        return total

''' 
    time complexity : O(n logn) + O(n)
    space complexity : O(1)
'''
