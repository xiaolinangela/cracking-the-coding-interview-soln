from LinkedList import LinkedListNode
from LinkedList import LinkedList
import math


def sum_lists(l1, l2):
    sum = sum_head = LinkedListNode(0)
    carry = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        digit_sum = val1 + val2 + carry
        sum.next = LinkedListNode(digit_sum % 10)
        sum = sum.next
        carry = int(math.floor(digit_sum/10))
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry == 1:
        sum.next = LinkedListNode(1)
    return sum_head.next


if __name__ == "__main__":
    l1 = LinkedList([7, 1, 6])
    l2 = LinkedList([5, 9, 2])
    result = sum_lists(l1.head, l2.head)
    while result:
        print(result.val)
        result = result.next
    result.printNode()
