class SortStack:

    def __init__(self):
        self.stack = []
        self.temp_stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        self.peek()
        print(self.temp_stack)
        return self.temp_stack.pop()
    
    def peek(self):
        while self.stack:
            if not self.temp_stack or self.temp_stack[-1] >= self.stack[-1]:
                self.temp_stack.append(self.stack.pop())
            elif self.temp_stack[-1] < self.stack[-1]:
                value = self.stack.pop()
                while self.temp_stack:
                    self.stack.append(self.temp_stack.pop())
                self.temp_stack.append(value)
        return self.temp_stack[-1]

if __name__ == "__main__":
    s = SortStack()
    s.push(1)
    s.push(98)
    s.push(2)
    s.push(23)
    s.push(10)
    print(s.pop())

