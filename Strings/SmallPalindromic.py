from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        counts = Counter(s)
        left_half = []
        middle_char = ""
        
        for char in sorted(counts.keys()):
            freq = counts[char]
            left_half.append(char * (freq // 2))
            if freq % 2 == 1:
                middle_char = char
                
        first_half_str = "".join(left_half)
        return first_half_str + middle_char + first_half_str[::-1]
