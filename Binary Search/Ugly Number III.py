from fractions import gcd
class Solution:
    def nthUglyNumber(self, n, a, b, c):
        def lcm(x, y):
            return (x * y) // gcd(x, y)
        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ca = lcm(c, a)
        lcm_abc = lcm(lcm_ab, c)
        def count_divisible(mid):
            return (mid // a + mid // b + mid // c 
                    - mid // lcm_ab - mid // lcm_bc - mid // lcm_ca 
                    + mid // lcm_abc)
        low = 1
        high = 2 * (10**18)  
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_divisible(mid) >= n:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1  
        return ans
