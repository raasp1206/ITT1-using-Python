from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        counts = Counter(s)
        sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return "".join(char * freq for char, freq in sorted_chars)
