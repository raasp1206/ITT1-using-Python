class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        # Sort words by length to process shorter potential components first
        words.sort(key=len)
        word_set = set()
        result = []
        def canForm(word, memo):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or canForm(suffix, memo):
                        memo[word] = True
                        return True
                        
            memo[word] = False
            return False

        for word in words:
            if not word:
                continue
            
            memo = {}
            if canForm(word, memo):
                result.append(word)
                
            word_set.add(word)
            
        return result
