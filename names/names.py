import time

class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, new_node):
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if not self.head and not self.tail:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif node is self.head:
            self.head = self.head.next
            self.length -= 1
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()
        

class LRUCache:
    def __init__(self, limit=10):
        if limit <= 0:
            print("Limit must be greater than 0")
        self.storage = {}
        self.list = DoublyLinkedList()
        self.limit = limit
        self.current_size = 0

    def get(self, key):
        if key not in self.storage:
            return None
        node = self.storage[key]

        if self.list.head == node:
            return node.value
        self.list.delete(node)
        self.list.add_to_head(node)
        return key

    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = value

            if self.list.head != node:
                deleted_node = node
                self.list.delete(node)
                self.list.add_to_head(deleted_node)
        else:
            new_node = ListNode(key, value)
            if self.current_size == self.limit:
                del self.storage[self.list.tail.key]
                self.list.delete(self.list.tail)
            self.list.add_to_head(new_node)
            self.storage[key] = new_node
            self.current_size += 1

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

lru = LRUCache(10000)
for index, name_1 in enumerate(names_1):
    lru.set(name_1, index)
for name_2 in names_2:
    duplicate = lru.get(name_2)
    if duplicate is not None:
        duplicates.append(duplicate)        

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
