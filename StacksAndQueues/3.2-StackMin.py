class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,value):
        self.stack.append(value)
        if self.min_stack[-1] >= value or not self.min_stack:
            self.min_stack[-1] = value
    
    def get_min(self):
        return self.min_stack[-1]
    
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack[-1].pop()
    
    def top(self):
        return self.stack[-1]

