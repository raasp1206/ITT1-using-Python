class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the shorter array to keep binary search efficient
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = half_len - i      # Partition index for nums2
            
            # Check if i is too small
            if i < m and nums2[j-1] > nums1[i]:
                low = i + 1
            # Check if i is too large
            elif i > 0 and nums1[i-1] > nums2[j]:
                high = i - 1
            # i is perfect!
            else:
                # Find max of left side
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                
                # If total length is odd, return max_left
                if (m + n) % 2 == 1:
                    return float(max_left)
                
                # Find min of right side
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                
                return (max_left + min_right) / 2.0
