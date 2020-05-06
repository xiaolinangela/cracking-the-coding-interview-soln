import heapq
class SetOfStacks:
    def __init__(self, capacity):
        self.c = capacity
        self.q = []
        self.stacks = []
    
    def push(self, val):
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q)
        if not self.q:
            heapq.heappush(self.q, len(self.stacks))
        if self.q[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)
    
    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.pop_at_stack(len(self.stacks)-1)
    
    def pop_at_stack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index)
            return self.stacks[index].pop()
        return -1

    def printStack(self):
        print(self.stacks)
if __name__ == "__main__":
    ss = SetOfStacks(2)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.pop_at_stack(2)
    ss.pop()
    ss.printStack()