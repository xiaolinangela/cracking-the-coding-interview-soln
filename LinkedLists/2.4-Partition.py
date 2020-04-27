from LinkedList import LinkedListNode
from LinkedList import LinkedList


def partition(head, x):
    before = before_head = LinkedListNode(0)
    after = after_head = LinkedListNode(0)
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next


if __name__ == "__main__":
    lList = LinkedList([1, 4, 3, 2, 5, 2])
    partition(lList.head, 3)
    lList.printNode()
