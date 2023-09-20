from dataclasses import dataclass


@dataclass
class Node:
    data: str = None
    next: str = None
    prev: str = None


@dataclass
class Doubly_linked_list:
    head: str = None

    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def print_dllst(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def insert(self, prev_node, new_data):
        if not prev_node:
            return
        new_node = Node(new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_end(self, new_data):
        last = self.head
        while last.next:
            last = last.next
        new_node = Node(new_data)
        new_node.next = None
        last.next = new_node
        new_node.prev = last


dlst = Doubly_linked_list()
A = Node("A")
B = Node("B")
C = Node("C")
dlst.head = A
A.next = B
B.prev = A
B.next = C
C.prev = B
dlst.insert_beginning("D")
dlst.insert(dlst.head, "E")
dlst.insert_end("F")
dlst.print_dllst()
