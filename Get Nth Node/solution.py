from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    current = node
    current_idx = 0
    while current is not None:
        if current_idx == index:
            return current
        current = current.next
        current_idx += 1
    raise Exception("Index out of range")
