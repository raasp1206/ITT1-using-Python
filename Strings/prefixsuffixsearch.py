class WordFilter:

    def __init__(self, words):
        self.lookup = {}

        for index, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                prefix = word[:i]
                for j in range(n + 1):
                    suffix = word[j:]
                    self.lookup[prefix + "#" + suffix] = index

    def f(self, pref, suff):
        return self.lookup.get(pref + "#" + suff, -1)
