# linear data structure made up of nodes and refs to the next node

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    def remove_tail(self):
        """
        remove the last node in the chain and return its value
        """
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
        else:
            value = self.tail.get_value()

            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()

            self.tail = current_node
            self.tail.set_next(None)
        self.length -= 1
        return value

    def remove_head(self):

        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
        self.length -= 1
        return value
    
    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    def output_list(self):
        """
        outputs the list (the value of the node)
        """
        current_node = self.head
        l = []
        while current_node is not None:
            l.append(current_node.value)

            current_node = current_node.get_next()
        return l

    def compare(self, other_list):
        
        l = LinkedList()
        current_node = other_list.head

        while current_node:
            if self.contains(current_node.value):
                l.add_to_tail(current_node.value)
            current_node = current_node.get_next()
        return l

