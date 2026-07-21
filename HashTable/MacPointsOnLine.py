import math

class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 0
        
        for i in range(n):
            slopes = {}
            local_max = 0
            x1, y1 = points[i] 
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1                
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slope_key = (dx, dy)
                
                slopes[slope_key] = slopes.get(slope_key, 0) + 1
                local_max = max(local_max, slopes[slope_key])
                
            max_points = max(max_points, local_max + 1)
            
        return max_points
