class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        max_result = []
        
        def getMaxSubsequence(nums, length):
            stack = []
            drop = len(nums) - length
            for num in nums:
                while drop > 0 and len(stack) > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        
        def merge(sub1, sub2):
            res = []
            i = j = 0
            while i < len(sub1) or j < len(sub2):
                if sub1[i:] > sub2[j:]:
                    res.append(sub1[i])
                    i += 1
                else:
                    res.append(sub2[j])
                    j += 1
            return res

        for i in xrange(max(0, k - n), min(k, m) + 1):
            sub1 = getMaxSubsequence(nums1, i)
            sub2 = getMaxSubsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > max_result:
                max_result = candidate
                
        return max_result
