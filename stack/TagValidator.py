class Solution(object):
    def isValid(self, code):
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and not stack:
                return False
            if code[i:i+9] == "<![CDATA[":
                if not stack:
                    return False
                j = code.find("]]>", i + 9)
                if j == -1:
                    return False
                i = j + 3 
            elif code[i:i+2] == "</":
                if not stack:
                    return False
                j = code.find(">", i + 2)
                if j == -1:
                    return False
                
                tag_name = code[i+2:j]
                if not (1 <= len(tag_name) <= 9) or not tag_name.isupper() or not tag_name.isalpha():
                    return False
                    
                if stack[-1] != tag_name:
                    return False
                    
                stack.pop()
                i = j + 1
                
            elif code[i] == "<":
                j = code.find(">", i + 1)
                if j == -1:
                    return False
                
                tag_name = code[i+1:j]
                if not (1 <= len(tag_name) <= 9) or not tag_name.isupper() or not tag_name.isalpha():
                    return False
                    
                stack.append(tag_name)
                i = j + 1
                
            else:
                if not stack:
                    return False
                i += 1
                
        return len(stack) == 0
