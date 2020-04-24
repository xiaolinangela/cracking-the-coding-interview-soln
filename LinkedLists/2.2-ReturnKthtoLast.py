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

def ReturnKthtoLast(k, head):
    p1 = head
    p2 = head
    for i in range (k):
        p1 = p1.next 
    while p1 != None:
        p1 = p1.next 
        p2 = p2.next
    return p2.val

if __name__ == "__main__":
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(1)
    fourth = Node(3)
    lList.head.next = second
    second.next = third
    third.next = fourth
    print(ReturnKthtoLast(2,lList.head))
