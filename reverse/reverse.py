class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node == self.head:
            cur = self.head
            while cur:
                print(cur.get_value())
                nxt = cur.get_next()
                cur.set_next(prev)
                prev = cur
                cur = nxt
            self.head = prev
        else:
            cur = node
            while cur:
                print(cur.get_value())
                nxt = cur.get_next()
                cur.set_next(prev)
                prev = cur
                cur = nxt
            node = prev 


list1 = LinkedList()
list1.add_to_head(1)
list1.add_to_head(2)
list1.add_to_head(3)

# print(list1.head.get_value())
# print(list1.head.get_next().get_value())
# print(list1.head.get_next().get_next().get_value())
# print(list1.reverse_list(list1.head, None))
