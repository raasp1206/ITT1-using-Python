class Solution(object):
    def calculate(self, s):
        stack = []
        current_result = 0
        sign = 1 
        i = 0
        n = len(s)
        last_token = '('
        
        while i < n:
            char = s[i]      
            if char == ' ':
                i += 1
                continue
                
            if char.isdigit():
                current_num = 0
                while i < n and s[i].isdigit():
                    current_num = current_num * 10 + int(s[i])
                    i += 1
                current_result += sign * current_num
                last_token = 'num'
                continue   
            elif char == '+':
                sign = 1
                last_token = '+'    
            elif char == '-':
                sign = -1
                last_token = '-'           
            elif char == '(':
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1
                last_token = '('
                
            elif char == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                current_result = prev_result + (prev_sign * current_result)
                last_token = ')'
                
            i += 1
            
        return current_result
