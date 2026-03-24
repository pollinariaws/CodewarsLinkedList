from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    current = head
    while current and current.next:
        a = current
        b = current.next
        a.next = b.next
        b.next = a
        if prev:
            prev.next = b
        prev = a
        current = a.next
    return new_head
