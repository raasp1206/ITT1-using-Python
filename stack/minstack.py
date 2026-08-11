class MinStack(object):

    def __init__(self):
        """Initializes the stack object."""
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """Pushes the element val onto the stack."""
        self.stack.append(val)
        # If min_stack is empty or val is <= the current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """Removes the element on the top of the stack."""
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        """Gets the top element of the stack."""
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """Retrieves the minimum element in the stack."""
        return self.min_stack[-1] if self.min_stack else None
