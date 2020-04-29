from LinkedList import LinkedList
from LinkedList import LinkedListNode


def is_palindrome(l1_head):
    def reversed_list(node):
        head = None
        while node:
            n = LinkedListNode(node.val)
            n.next = head
            head = n
            node = node.next
        return head
    l1_reversed = reversed_list(l1_head)
    while l1_head and l1_reversed:
        if l1_head.val != l1_reversed.val:
            return False
        l1_head = l1_head.next
        l1_reversed = l1_reversed.next
    return True


if __name__ == "__main__":
    lList = LinkedList([1, 2])
    lList_1 = LinkedList([0, 0])
    lList_2 = LinkedList([1, 2, 2, 1])
    lList_3 = LinkedList([])
    print(is_palindrome(lList.head))
    print(is_palindrome(lList_1.head))
    print(is_palindrome(lList_2.head))
    print(is_palindrome(lList_3.head))
