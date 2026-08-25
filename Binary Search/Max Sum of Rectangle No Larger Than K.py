import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        max_sum = float('-inf')

        for left in range(n):
            row_sums = [0] * m
            
            for right in range(left, n):
                for r in range(m):
                    row_sums[r] += matrix[r][right]

                prefix_sums = [0]
                current_prefix_sum = 0
                
                for val in row_sums:
                    current_prefix_sum += val

                    target = current_prefix_sum - k
                    idx = bisect.bisect_left(prefix_sums, target)
                    
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, current_prefix_sum - prefix_sums[idx])
                        
                    if max_sum == k:
                        return k
                    bisect.insort(prefix_sums, current_prefix_sum)
                    
        return max_sum
