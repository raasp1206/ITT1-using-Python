from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        dq = deque()
        max_value = float('-inf')
        
        for xj, yj in points:
            while dq and xj - dq[0][1] > k:
                dq.popleft()
                
            if dq:
                max_value = max(max_value, dq[0][0] + yj + xj)
                
            current_diff = yj - xj
            while dq and dq[-1][0] <= current_diff:
                dq.pop()
                
            dq.append((current_diff, xj))
            
        return max_value
