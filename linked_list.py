from dataclasses import dataclass


@dataclass
class Node:
    value: str = None
    next_value: str = None


@dataclass
class LinkedList:
    head_val: str = None

    def print_values(self):
        val = self.head_val
        while val is not None:
            print(val.value)
            val = val.next_value

    def insert_at_beginning(self, new):
        newNode = Node(new)
        newNode.next_value = self.head_val
        self.head_val = newNode

    def insert_at_end(self, new):
        newNode = Node(new)
        last_node = self.head_val
        while last_node.next_value is not None:
            last_node = last_node.next_value
        last_node.next_value = newNode


lst = LinkedList()
lst.head_val = Node("1")
a = Node("2")
b = Node("3")
lst.head_val.next_value = a
a.next_value = b

lst.print_values()
lst.insert_at_beginning("4")
lst.print_values()
lst.insert_at_end("5")
lst.print_values()
