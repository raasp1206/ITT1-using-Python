class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [0] * n
        ugly[0] = 1  
        i2 = i3 = i5 = 0  
        for i in range(1, n):
            next_2 = ugly[i2] * 2
            next_3 = ugly[i3] * 3
            next_4 = ugly[i5] * 5
            next_ugly = min(next_2, next_3, next_4)
            ugly[i] = next_ugly
            if next_ugly == next_2:
                i2 += 1
            if next_ugly == next_3:
                i3 += 1
            if next_ugly == next_4:
                i5 += 1
                
        return ugly[-1]
