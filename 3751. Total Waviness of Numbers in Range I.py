class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            d = str(num)
            for i in range(1, len(d) - 1):
                if d[i] > d[i-1] and d[i] > d[i+1]:   # peak
                    total += 1
                elif d[i] < d[i-1] and d[i] < d[i+1]: # valley
                    total += 1
        return total

'''
    for each number in range, check middle digits
    peak: digit strictly greater than both neighbors
    valley: digit strictly less than both neighbors
    first/last digits excluded (no two neighbors)
    constraint num2 <= 10^5 makes brute force fine
    time complexity : O((num2 - num1) * digits)
    space complexity : O(1)
'''
