from LinkedList import LinkedList
from LinkedList import LinkedListNode

class AnimalShelter:

    def __init__(self):
        self.dog = LinkedList()
        self.cat = LinkedList()
        self.order = 0

    def enqueue(self,animal,type):
        if type == "dog":
            self.dog.add([animal],"dog",self.order)
            self.order += 1
        else:
            self.cat.add([animal], "cat", self.order)
            self.order += 1
    
    def dequeue_any(self):
        if self.dog.head.order < self.cat.head.order:
            self.dog.head = self.dog.head.next
        else:
            self.cat.head = self.cat.head.next

    def dequeue_dog(self):
        self.dog.head = self.dog.head.next 

    def dequeue_cat(self):
        self.cat.head = self.cat.head.next 

if __name__ == "__main__":
    a = AnimalShelter()
    a.enqueue("dog1", "dog")
    a.enqueue("cat1","cat")
    a.enqueue("dog2","dog")
    a.dog.printNode()
    a.cat.printNode() 
    a.dequeue_any()
    a.dequeue_dog()
    a.dog.printNode()
    a.cat.printNode()

