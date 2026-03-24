from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(' -> ')
    if parts[0] == 'None':
        return None
    head = Node(int(parts[0]))
    current = head
    for part in parts[1:]:
        if part != 'None':
            current.next = Node(int(part))
            current = current.next
    return head
