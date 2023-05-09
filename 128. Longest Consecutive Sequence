class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums :
            if n-1 not in numSet :
                length = 0
                while (n+length) in numSet :
                    length += 1
                longest = max(longest, length)
        return longest 
    """ time complexity O(N)
        space complexity O(N)"""
    #   nums = [100,4,200,1,3,2] for this ----1,2,3,4-----100-----200---- imaginary line 




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        dit = {}
        longest = 0
        for i in nums :
            dit[i] = False
        for i in nums :
            next_num = i+1
            prev_num = i-1
            dit[i] = True
            curr_len = 1
            while next_num in dit and dit[next_num] == False :
                curr_len += 1
                dit[next_num] = True
                next_num += 1
            while prev_num in dit and dit[prev_num] == False :
                curr_len += 1
                dit[prev_num] = True
                prev_num -= 1

            longest = max(longest, curr_len)
        return longest
        """ we can  get the solution in single itearation using hashmap (dictionary in python). here we are checking both right and left values for unseen/unvisited values"""


# O(n logn) time constant space  and using sorting 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        nums.sort()
        nums.append((-10 ** 9) - 1)
        res = 0
        c = 1
        for i in range(n) :
            if nums[i] + 1 == nums[i+1] :
                c += 1
            else :
                c = 1
            res = max(res, c)
        return res
