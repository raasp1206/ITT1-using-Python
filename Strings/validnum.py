class Solution(object):
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        s = s.strip()
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                    
            elif char in ('e', 'E'):
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
                
            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            else:
                return False
        return seen_digit
