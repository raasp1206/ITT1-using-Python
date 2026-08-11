class Solution(object):
    def removeDuplicateLetters(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        stack = []
        seen = set() 
        for char in s:
            count[char] -= 1
            
            if char in seen:
                continue
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed_char = stack.pop()
                seen.remove(removed_char)
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
