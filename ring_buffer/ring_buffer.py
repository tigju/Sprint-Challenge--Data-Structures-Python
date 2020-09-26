# Array data structure implementation

# class RingBuffer:
#     def __init__(self, capacity):
#         self.buff = []
#         self.capacity = capacity
#         self.size = 0
#         self.pointer = 0

#     def append(self, item):
#         if self.size < self.capacity:
#             self.buff.append(item)
#             self.size += 1
#         else:
#             if self.pointer >= self.capacity:
#                 self.pointer = 0
#             self.buff.pop(self.pointer)
#             self.buff.insert(self.pointer, item)
#             self.pointer +=1

#     def get(self):
#         return [i for i in self.buff if i is not None]


# Singly Linked List data structure implementation

class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.pointer = self.head
        

    def append(self, item):
        new_node = Node(item)
        # if storage current size less then capacity
        if self.size < self.capacity:
            if self.head is None or self.tail is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node
            self.size += 1
            self.pointer = new_node
        # if capacity equals or greater than size
        else:
            if self.pointer == self.tail:
                self.pointer = self.head
                self.tail = new_node
                new_node.next_node = self.pointer
            if self.pointer == self.head:
                self.pointer = self.head.next_node
                self.head = new_node
                new_node.next_node = self.pointer
            else:
                # print("current pointer", self.pointer.value)
                if self.pointer.next_node == None:
                    old_pointer_next = self.head
                else:
                    old_pointer_next = self.pointer.next_node
                
                self.pointer.value = new_node.value
                self.pointer = old_pointer_next
                            
                # print("next pointer", self.pointer.value)
                # print("new node", new_node.value)

            
    def get(self):
        l = []
        curr = self.head
        while curr:
            l.append(curr.value)
            curr = curr.next_node
        return l


r = RingBuffer(6)
r.append('a')
print(r.get())
r.append('b')
print(r.get())
r.append('c')
print(r.get())
r.append('d')
print(r.get())
r.append('e')
print(r.get())
r.append('1')
print(r.get())
r.append('2')
print(r.get())
r.append('3')
print(r.get())
r.append('4')
print(r.get())
r.append('5')
print(r.get())
r.append('6')
print(r.get())
r.append('7')
print(r.get())
r.append('8')
print(r.get())
r.append('9')
print(r.get())
