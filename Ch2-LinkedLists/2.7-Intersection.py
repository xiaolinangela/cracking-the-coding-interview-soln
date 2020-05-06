from LinkedList import LinkedListNode
from LinkedList import LinkedList


def intersection(headA, headB):
    def get_len(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    len1 = get_len(headA)
    len2 = get_len(headB)
    if len2 > len1:
        headA, headB = headB, headA
        len1, len2 = len2, len1
    for i in range(len1-len2):
        headA = headA.next
    while headA.val != headB.val:
        headA = headA.next
        headB = headB.next
    return headA


if __name__ == "__main__":
    listA = LinkedList([4, 1, 8, 4, 5])
    listB = LinkedList([5, 0, 1, 8, 4, 5])
    result = intersection(listA.head, listB.head)
    print(result)
    while result:
        print(result.val)
        result = result.next
