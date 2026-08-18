class Solution(object):
    def minimumCoins(self, prices):
        n = len(prices)
        dp = [0] * (n + 2)
        for i in range(n, 0, -1):
            if 2 * i >= n:
                dp[i] = prices[i - 1]
            else:
                next_min_cost = min(dp[j] for j in range(i + 1, 2 * i + 2))
                dp[i] = prices[i - 1] + next_min_cost
                
        return dp[1]
