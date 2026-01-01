class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

''' 
  time complexity : O(n)
  space complexity : O(1)
'''

######################################################################################################################################################

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            
            if carry == 0:
                break

        if carry:
            digits.insert(0, 1)
        
        return digits

''' 
  time complexity : O(n)
  space complexity : O(1)
'''

