class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        len1, len2 = len(s1), len(s2)
        seen = {}
        s2_count = 0
        s2_idx = 0
        
        for i in xrange(n1):
            for j in xrange(len1):
                if s1[j] == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len2:
                        s2_count += 1
                        s2_idx = 0
            
            if s2_idx in seen:
                prev_i, prev_s2_count = seen[s2_idx]
                cycle_blocks = i - prev_i
                cycle_s2_count = s2_count - prev_s2_count
                
                remaining_blocks = n1 - 1 - i
                num_cycles = remaining_blocks // cycle_blocks
                
                s2_count += num_cycles * cycle_s2_count
                leftover_blocks = remaining_blocks % cycle_blocks
                
                for _ in xrange(leftover_blocks):
                    for j in xrange(len1):
                        if s1[j] == s2[s2_idx]:
                            s2_idx += 1
                            if s2_idx == len2:
                                s2_count += 1
                                s2_idx = 0
                return s2_count // n2
            
            seen[s2_idx] = (i, s2_count)
            
        return s2_count // n2
