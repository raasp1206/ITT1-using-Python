class Solution(object):
    def deserialize(self, s):
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))   
        stack = []
        num_str = ""
        
        for i, char in enumerate(s):
            if char == '[':
                stack.append(NestedInteger())
            elif char == '-' or char.isdigit():
                num_str += char
            elif char in (',', ']'):
                if num_str:
                    stack[-1].add(NestedInteger(int(num_str)))
                    num_str = ""
                if char == ']' and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)
                    
        return stack[0]
