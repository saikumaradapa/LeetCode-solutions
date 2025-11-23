
# run current_sum 
# if current_sum is (useless to sum) negative then restart current_sum 
# take max_sum_so_far from current_sum

# O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]

        for n in nums :
            cur_sum  += n
            cur_sum = max(cur_sum, n) 
            max_sum = max(max_sum, cur_sum)
        return max_sum



# O(N^2) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = nums[0]
        for j in range(len(nums)) :
            sum = 0
            for i in range(j,len(nums)) :
                sum += nums[i]
                max_s = max(max_s, sum)
            #     print(sum)
            # print(' ')
        return max_s
