class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    first = head
    second = head.next
    current = head
    while current and current.next:
        a = current
        b = current.next
        if b.next:
            a.next = b.next
            b.next = b.next.next
        else:
            a.next = None
            b.next = None
        current = a.next
    return Context(first, second)
