class LinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getNextNode(self):
        return self.next


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values != None:
            self.add_multiple(values)

    def printNode(self):
        curr = self.head
        list = []
        while curr:
            list.append(curr.val)
            curr = curr.getNextNode()
        print(list)

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def add(self, value):
        if self.head == None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def __len__(self):
        curr = self.head
        result = 0
        while curr:
            result += 1
            curr = curr.next
        return result


if __name__ == "__main__":
    l1 = LinkedList([3, 4, 5])
    l1.printNode()
    print(len(l1))
