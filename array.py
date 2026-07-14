from collections import Counter
class Solution(object):
    def canReorderDoubled(self, arr):
        count = Counter(arr)
        sorted_keys = sorted(count.keys(), key=abs)
        for x in sorted_keys:
            if count[x] == 0:
                continue                
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]   
        return True
