class LinkedListNode:
    def __init__(self, x, type, order):
        self.val = x
        self.next = None
        self.type = type
        self.order = order


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

    def add(self, value,type,order):
        if self.head == None:
            self.head = self.tail = LinkedListNode(value,type,order)
        else:
            self.tail.next = LinkedListNode(value,type,order)
            self.tail = self.tail.next
        return self.tail

