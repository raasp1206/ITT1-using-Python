from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        results = []
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_count[word] += 1
                    while current_count[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    if right - left == total_len:
                        results.append(left)
                else:
                    current_count.clear()
                    left = right                    
        return results
