class Solution(object):
    def maxSum(self, nums1, nums2):
        MOD = 10**9 + 7
        m, n = len(nums1), len(nums2)
        
        i, j = 0, 0
        sum1, sum2 = 0, 0
        total_max_sum = 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                total_max_sum += max(sum1, sum2) + nums1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
                
        while i < m:
            sum1 += nums1[i]
            i += 1
            
        while j < n:
            sum2 += nums2[j]
            j += 1
            
        total_max_sum += max(sum1, sum2)
        
        return total_max_sum % MOD
