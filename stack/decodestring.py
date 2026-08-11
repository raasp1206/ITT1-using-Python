class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Form the full multiplier (handles multi-digit numbers like 12[a])
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current state to the stack and reset trackers
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the previous string and the repeat count
                last_string, num = stack.pop()
                # Multiply the enclosed string and append to the outer string
                current_string = last_string + (current_string * num)
            else:
                # Append standard letters to the current working string
                current_string += char
                
        return current_string
