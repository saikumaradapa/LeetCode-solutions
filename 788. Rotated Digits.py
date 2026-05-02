class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(num):
            str_num = str(num)
            if '3' in str_num or '4' in str_num or '7' in str_num:
                return False
            if '2' in str_num or '5' in str_num or '6' in str_num or '9' in str_num:
                return True
            return False

        res = 0
        for i in range(1, n + 1):
            if is_good(i):
                res += 1
        return res

'''
    a number is "good" if:
    - no invalid digits (3, 4, 7)
    - at least one digit that changes on rotation (2, 5, 6, 9)
    digits 0, 1, 8 are valid but don't change
    time complexity : O(n * d) where d = number of digits
    space complexity : O(d)
'''
