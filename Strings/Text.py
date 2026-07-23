class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            line = []
            line_len = 0

            # Pack as many words as possible
            while i < len(words) and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1

            # Last line or line with one word
            if i == len(words) or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                spaces = maxWidth - line_len
                gaps = len(line) - 1

                even = spaces // gaps
                extra = spaces % gaps

                s = ""
                for j in range(gaps):
                    s += line[j]
                    s += " " * (even + (1 if j < extra else 0))
                s += line[-1]

                res.append(s)

        return res
