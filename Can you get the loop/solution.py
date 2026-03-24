def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    count = 0
    current = slow
    while True:
        current = current.next
        count += 1
        if current == slow:
            break
    return count
