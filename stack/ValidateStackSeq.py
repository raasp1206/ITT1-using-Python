class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        pop_index = 0
        
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return len(stack) == 0
