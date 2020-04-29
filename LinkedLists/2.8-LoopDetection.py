def loop_detection(head):
    dict = {}
    while head:
        if head not in dict:
            dict[head] = 1
            head = head.next
        else:
            return True
    return False


def loop_detection_2pointers(head):
    if head == None or head.next == None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
