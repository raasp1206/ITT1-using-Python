import random

class Solution:

    def __init__(self, n, blacklist):
        self.size = n - len(blacklist)
        self.mapping = {}

        black = set(blacklist)
        last = n - 1

        for b in blacklist:
            if b < self.size:
                while last in black:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        x = random.randint(0, self.size - 1)
        return self.mapping.get(x, x)
