class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            temp = []
            while num:
                temp.append(num % 10)
                num //= 10
            res.extend(temp[::-1])
        return res

'''
    extract digits using mod 10, reverse since we get them backwards
    time complexity : O(total digits)
    space complexity : O(total digits)
'''
