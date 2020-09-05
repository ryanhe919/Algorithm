def reversePrint(head):
    result = []
    while head != None:
        result.append(head.val)
        head = head.next
    result.reverse()
    return result