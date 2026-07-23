class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)

        # If lengths don't match, it's impossible
        if m + n != len(s3):
            return False

        # dp[i][j] = True if s3[:i+j] can be formed
        # using s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # First column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # First row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[m][n]
