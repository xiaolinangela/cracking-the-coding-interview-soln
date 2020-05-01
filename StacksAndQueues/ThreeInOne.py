class Multistack:
    
    def __init__(self, stacksize):
        self.numstacks = 3
        self.values = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.capacity = stacksize

    def push(self, stacknum, value):
        if(is_full(self, stacknum)):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        values[indexOfTop(stacknum)] = value 
    
    def pop(self, stacknum):
    
    def peek(self, stacknum):
    
    def is_empty(self, stacknum):
    
    def is_full(self, stacknum):
    
    def index_of_top(self, stacknum):
        

