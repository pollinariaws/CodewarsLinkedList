class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def recurse(current, prev):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return recurse(next_node, current)
    return recurse(head, None)
