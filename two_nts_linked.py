def add_integers(integer1, integer2):
    result = None
    last = None
    carry = 0
    while integer1 != None or integer2 != None or carry > 0:
        first = 0 if integer1 == None else integer1.data
        second = 0 if integer2 == None else integer2.data
        sum = first + second + carry
        pNew = LinkedListNode(sum % 10)
        carry = sum // 10
        if result == None:
            result = pNew
        else:
            last.next = pNew

        last = pNew
        if integer1 != None:
            integer1 = integer1.next

        if integer2 != None:
            integer2 = integer2.next

    return result


first = create_linked_list([1, 2, 3])  # 321
second = create_linked_list([1, 2])  # 21
print("Sum:")
result = add_integers(first, second)
display(result)
