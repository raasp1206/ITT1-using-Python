class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word_id = -1
        # Stores indices of all words whose remaining suffix forms a palindrome
        self.palindrome_suffixes = []

class Solution(object):
    def palindromePairs(self, words):
        root = TrieNode()
        pairs = []        
        def is_palindrome(word, start, end):
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True
        for idx, word in enumerate(words):
            node = root
            for j in range(len(word) - 1, -1, -1):
                if is_palindrome(word, 0, j):
                    node.palindrome_suffixes.append(idx)
                    
                char = word[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                
            node.word_id = idx
            node.palindrome_suffixes.append(idx)
        for idx, word in enumerate(words):
            node = root
            has_failed = False
            
            for j in range(len(word)):
                if node.word_id != -1 and node.word_id != idx:
                    if is_palindrome(word, j, len(word) - 1):
                        pairs.append([idx, node.word_id])
                        
                char = word[j]
                if char not in node.children:
                    has_failed = True
                    break
                node = node.children[char]
                
            if has_failed:
                continue
            for remaining_idx in node.palindrome_suffixes:
                if remaining_idx != idx:
                    pairs.append([idx, remaining_idx])
                    
        return pairs
