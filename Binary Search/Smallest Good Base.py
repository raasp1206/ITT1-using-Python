class Solution:
    def smallestGoodBase(self, n):
        num = int(n)

        max_m = len(bin(num)) - 2
        for m in range(max_m, 1, -1):

            low = 2
            high = int(num ** (1.0 / (m - 1))) + 1
            
            while low <= high:
                mid = (low + high) // 2

                current_sum = 0
                for _ in range(m):
                    current_sum = current_sum * mid + 1
                    
                if current_sum == num:
                    return str(mid)
                elif current_sum > num:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return str(num - 1)
