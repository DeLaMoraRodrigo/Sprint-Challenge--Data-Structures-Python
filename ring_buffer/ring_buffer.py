class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_node = None
        self.return_buffer = []
        self.list = DoublyLinkedList()
        self.current_size = 0

    def append(self, item):
        if self.current_size < self.capacity:
            self.list.add_to_tail(item)
            self.current_size += 1
            if self.current_size == 1:
                self.oldest_node = self.list.head
        else:
            self.oldest_node.value = item
            if self.oldest_node is self.list.tail:
                self.oldest_node = self.list.head
            else:
                self.oldest_node = self.oldest_node.next

    def get(self):
        node = self.list.head

        while node:
            self.return_buffer.append(node.value)
            node = node.next
        
        return self.return_buffer