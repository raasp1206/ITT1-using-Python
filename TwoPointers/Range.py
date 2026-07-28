class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7
        
        def get_count_and_sum(target):
            count = 0
            current_window_sum = 0
            total_subarrays_sum = 0
            running_window_value_sum = 0
            
            l = 0
            for r in xrange(n):
                current_window_sum += nums[r]
                running_window_value_sum += nums[r] * (r - l + 1)
                
                while current_window_sum > target:
                    running_window_value_sum -= current_window_sum
                    current_window_sum -= nums[l]
                    l += 1
                    
                count += (r - l + 1)
                total_subarrays_sum += running_window_value_sum
                
            return count, total_subarrays_sum

        def sum_of_first_k(k):
            if k == 0:
                return 0
            low, high = min(nums), sum(nums)
            k_th_value = high
            
            while low <= high:
                mid = (low + high) // 2
                count, _ = get_count_and_sum(mid)
                if count >= k:
                    k_th_value = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            count, total_sum = get_count_and_sum(k_th_value)
            return total_sum - (count - k) * k_th_value

        ans = sum_of_first_k(right) - sum_of_first_k(left - 1)
        return ans % MOD
