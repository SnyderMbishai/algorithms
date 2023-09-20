from dataclasses import dataclass


@dataclass
class Node:
    data: str = None
    next: str = None


@dataclass()
class SLLIst:
    head: str = None

    def list_print(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next

    def insert_begining(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert_between(self, mid, x):
        if not mid:
            return
        new_node = Node(x)
        new_node.next = mid.next
        mid.next = new_node
        pass

    def remove(self, x):
        head_val = self.head
        if head_val:
            if head_val.data == x:
                self.head = head_val.next
                head_val = None
                return

        while head_val:
            if head_val.data == x:
                break
            prev = head_val
            head_val = head_val.next

        if not head_val:
            return

        prev.next = head_val.next
        head_val = None


lst = SLLIst()
A = Node(data="20")
B = Node(data="30")
lst.head = A
A.next = B
print(lst)
lst.insert_begining("40")
lst.insert_end("50")
lst.insert_between(lst.head.next, "25")
lst.remove("25")
lst.list_print()
