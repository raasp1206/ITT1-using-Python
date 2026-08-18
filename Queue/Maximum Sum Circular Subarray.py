class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = 0
        
        max_sum = nums[0]
        current_max = 0
        
        min_sum = nums[0]
        current_min = 0
        
        for num in nums:
            total_sum += num
            
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum
            
        return max(max_sum, total_sum - min_sum)
