class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Step 1: Sort by end ascending, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Initialize the two largest points tracking our set
        p1 = -1
        p2 = -1
        ans = 0
        
        # Step 2: Greedily evaluate each interval
        for s, e in intervals:
            # Case 1: Current set has 0 points in this interval
            if s > p2:
                p1 = e - 1
                p2 = e
                ans += 2
            # Case 2: Current set has exactly 1 point (p2) in this interval
            elif s > p1:
                p1 = p2
                p2 = e
                ans += 1
            # Case 3: s <= p1, meaning both p1 and p2 are inside. Do nothing.
                
        return ans
