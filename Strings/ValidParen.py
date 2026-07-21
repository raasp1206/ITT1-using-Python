class Solution:
    def checkValidString(self, s: str) -> bool:
        o_count = 0
        c_count = 0
        length = len(s) - 1
        for i in range(length + 1):
            if s[i] == '(' or s[i] == '*':
                o_count += 1
            else:
                o_count -= 1
            if s[length - i] == ')' or s[length - i] == '*':
                c_count += 1
            else:
                c_count -= 1
            if o_count < 0 or c_count < 0:
                return False
        return True
