
# run current_sum 
# if current_sum is (useless to sum) negative then restart current_sum 
# take max_sum_so_far from current_sum

# O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> Tuple[int, int, int]:
        cur_sum = nums[0]
        max_sum = nums[0]
        start = 0
        end = 0
        temp_start = 0

        for i in range(1, len(nums)):
            if cur_sum + nums[i] < nums[i]:
                cur_sum = nums[i]
                temp_start = i
            else:
                cur_sum += nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
                start = temp_start
                end = i
        print(start, end)
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
