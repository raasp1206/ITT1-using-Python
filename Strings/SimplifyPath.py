class Solution:
    def simplifyPath(self, path):
        stack = []

        # Split the path by '/'
        for part in path.split('/'):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
