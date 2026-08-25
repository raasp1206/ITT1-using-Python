import collections
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(list(set(arr2)))
        dp = {-1: 0}
        
        for current_val in arr1:
            next_dp = collections.defaultdict(lambda: float('inf'))
            
            for prev_val in dp:
                if current_val > prev_val:
                    next_dp[current_val] = min(next_dp[current_val], dp[prev_val])
                
                idx = bisect.bisect_right(arr2, prev_val)
                if idx < len(arr2):
                    next_dp[arr2[idx]] = min(next_dp[arr2[idx]], dp[prev_val] + 1)
            
            if not next_dp:
                return -1            
            dp = next_dp
        min_ops = min(dp.values())
        return min_ops if min_ops != float('inf') else -1
