class Solution(object):
    def minimumPartitionScore(self, nums, k):
        n = len(nums)
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        def get_cost(i, j):
            s = pref[j + 1] - pref[i]
            return (s * (s + 1)) // 2
            
        dp = [[float('inf')] * n for _ in range(k + 1)]
        
        for j in range(n):
            dp[1][j] = get_cost(0, j)
            
        for i in range(2, k + 1):
            for j in range(i - 1, n):
                for m in range(i - 2, j):
                    cost = dp[i - 1][m] + get_cost(m + 1, j)
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        
        return dp[k][n - 1]
