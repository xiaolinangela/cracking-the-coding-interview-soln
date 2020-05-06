
from LinkedList import LinkedList

def delete_middle_node(node):
    node.value = node.next.val
    node.next = node.next.next 

if __name__ == "__main__":
    lList = LinkedList([1,2,3])
    middlenode = lList.add(4)
    lList.add_multiple([5,6,7])
    lList.printNode()
    delete_middle_node(middlenode)  
    lList.printNode()  