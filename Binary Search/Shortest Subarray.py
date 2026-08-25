from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
        min_len = n + 1
        dq = deque()  
        for i in range(n + 1):
            while dq and P[i] - P[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            while dq and P[i] <= P[dq[-1]]:
                dq.pop()
            dq.append(i)
        return min_len if min_len <= n else -1
