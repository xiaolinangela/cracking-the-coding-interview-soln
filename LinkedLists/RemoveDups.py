class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
    def getNextNode(self):
       return self.next

class LinkedList():
    def __init__(self):
        self.head = None
    def printNode(self):
       curr = self.head
       while curr:
           print(curr.val)
           curr = curr.getNextNode()

def remove_dups(lList):
    d = {}
    if lList.head == None:
        return lList
    current = lList.head.next
    prev = lList.head
    d[prev.val] = 0
    while current != None:
        if current.val in d:
            prev.next = current.next
            current = current.next
        else:
            d[current.val] = 0
            prev = current
            current = current.next 
    #print(d)
    return lList 

if __name__ == "__main__":
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(1)
    fourth = Node(3)
    lList.head.next = second
    second.next = third
    third.next = fourth
    remove_dups(lList)
    lList.printNode()     
        

