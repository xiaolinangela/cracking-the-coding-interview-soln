class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, val):
        self.s1.append(val)
    
    def pop(self):
        self.peek()
        return self.s2.pop()
    
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def is_empty(self):
        return not self.s1 and not self.s2

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.peek())
    print(q.is_empty())
