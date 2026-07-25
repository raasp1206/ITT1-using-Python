class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(word, pattern):
            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):
                if w in w_to_p:
                    if w_to_p[w] != p:
                        return False
                else:
                    w_to_p[w] = p

                if p in p_to_w:
                    if p_to_w[p] != w:
                        return False
                else:
                    p_to_w[p] = w

            return True

        result = []

        for word in words:
            if match(word, pattern):
                result.append(word)

        return result
