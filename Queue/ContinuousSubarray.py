from collections import deque

class Solution(object):
    def continuousSubarrays(self, nums):
        max_dq = deque()
        min_dq = deque()
        
        left = 0
        total_subarrays = 0
        
        for right in range(len(nums)):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            
            while nums[max_dq[0]] - nums[min_dq[0]] > 2:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
                    
            total_subarrays += (right - left + 1)
            
        return total_subarrays
