class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Task 1
def prepend(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node


# Task 2
def append(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


# Task 3
def remove_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


# Task 4
def print_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements) + " -> null")


# Task 5
def search(head, target):
    current = head
    index = 0
    while current:
        if current.data == target:
            return index
        current = current.next
        index += 1
    return -1


# Task 6
def insert_at(head, value, position):
    new_node = Node(value)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of range")
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head


# Task 7
def remove_value(head, target):
    if head is None:
        return None
    if head.data == target:
        return head.next
    prev = head
    current = head.next
    while current:
        if current.data == target:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    return head


# Task 8
def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    current = head1
    while current.next:
        current = current.next
    current.next = head2
    return head1

# Task 9
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


head = None
head = append(head, 1)
head = append(head, 2)
head = append(head, 3)
head = append(head, 4)
head = append(head, 5)

print("Исходный список:")
print_list(head)

print("Task 1 - prepend(0):")
head = prepend(head, 0)
print_list(head)

print("Task 2 - append(6):")
head = append(head, 6)
print_list(head)

print("Task 3 - remove_last:")
head = remove_last(head)
print_list(head)

print("Task 4 - print_list:")
print_list(head)

print("Task 5 - search(3):")
print(search(head, 3))

print("Task 6 - insert_at(10, position=2):")
head = insert_at(head, 10, 2)
print_list(head)

print("Task 7 - remove_value(10):")
head = remove_value(head, 10)
print_list(head)

print("Task 8 - merge с [7, 8, 9]:")
head2 = None
head2 = append(head2, 7)
head2 = append(head2, 8)
head2 = append(head2, 9)
head = merge(head, head2)
print_list(head)

print("Task 9 - reverse:")
head = reverse(head)
print_list(head)