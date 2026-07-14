from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        num_strs = [str(num) for num in nums]
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1 
            else:
                return 1  
        num_strs.sort(key=cmp_to_key(compare))
        
        ans = ''.join(num_strs)
        
        return '0' if ans[0] == '0' else ans
