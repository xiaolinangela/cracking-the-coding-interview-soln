from LinkedList import LinkedListNode
from LinkedList import LinkedList


def insert_before(list, data):
    node = LinkedListNode(data)
    if list:
        node.next = list
    return node


def pad_list(head, padding):
    head = insert_before(head, 0)
    return head


def add_lists(l1, l2, len1, len2):
    if(len1 < len2):
        l1 = pad_list(l1, len2-len1)
    else:
        l2 = pad_list(l2, len1-len2)

    def add_list_helper(l1, l2):
        if l1 == None and l2 == None:
            carry = 0
            sum = None
            return sum, carry
        result = add_list_helper(l1.next, l2.next)
        sum = result[0]
        carry = result[1]
        val = carry + l1.val + l2.val
        full_result = insert_before(sum, val % 10)
        sum = full_result
        carry = val/10
        return sum, carry
    c = add_list_helper(l1, l2)
    sum = c[0]
    carry = c[1]
    if carry == 0:
        return sum
    else:
        result = insert_before(sum, carry)
        return result


def add_lists_naive(l1, l2):
    str1, str2 = '', ''
    while l1:
        str1 += str(l1.val)
        l1 = l1.next
    while l2:
        str2 += str(l2.val)
        l2 = l2.next
    num = str(int(str1) + int(str2))
    dummy = dummy_head = LinkedListNode(0)
    for i in range(len(num)):
        dummy.next = LinkedListNode(num[i])
        dummy = dummy.next
    return dummy_head.next


if __name__ == "__main__":
    l1 = LinkedList([1, 7, 1, 6])
    l2 = LinkedList([5, 9, 2, 5, 6])
    len1 = len(l1)
    len2 = len(l2)
    result = add_lists(l1.head, l2.head, len1, len2)
    str1 = ""
    while result:
        str1 += str(result.val)
        result = result.next
    print(str1)
