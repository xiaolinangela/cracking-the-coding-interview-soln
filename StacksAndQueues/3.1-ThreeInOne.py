class Multistack:
    
    def __init__(self, stacksize):
        self.numstacks = 3
        self.values = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.capacity = stacksize

    def push(self, stacknum, value):
        if(self.is_full(stacknum)):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.values[self.index_of_top(stacknum)] = value 
    
    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        else:
            value = self.values[self.indexOfTop(stacknum)]
            self.values[self.index_of_top(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        return self.values[self.index_of_top(stacknum)]
    
    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0
    
    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.capacity
    
    def index_of_top(self, stacknum):
        self.offset = stacknum * self.capacity
        return self.offset + self.sizes[stacknum] - 1
    
    def print_array(self):
        return self.values

if __name__ == "__main__":
    stack1 = Multistack(2)
    stack1.push(2,13)
    print(stack1.peek(2))
    print(stack1.is_empty(2))
    print(stack1.is_full(2))
    stack1.push(2,14)
    print(stack1.print_array())
    




