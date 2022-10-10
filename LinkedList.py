class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def traverse(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            head = self.head
            while head is not None:
                print(head, end=" ")
                head = head.next
            print("\n")

    def insert_at_beginning(self, new_node):
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            head = self.head
            last_node = None
            while head is not None:
                last_node = head
                head = head.next
            last_node.next = new_node
        self.length += 1

    def insert_at_specific_position(self, new_node, position):
        if self.head is None and position > 0:
            print(f"Linked list is empty. Position {position} is not available in the LinkedList.")
        elif self.head is None and position == 0:
            self.head = new_node
        elif position > self.length:
            print(f"Can not insert at index {position} for a LinkedList with {self.length} size.")
        else:
            current_position = 0
            head = self.head

            if position == 0:
                new_node.next = head
                self.head = new_node
                self.length += 1
                return

            while head is not None:
                current_position += 1
                if current_position == position:
                    break
                else:
                    head = head.next

            new_node.next = head.next
            head.next = new_node
            self.length += 1

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1

    def delete_from_end(self):
        if self.head is None:
            print("LinkedList is empty. Nothing is available to delete.")
        # traverse till end
        head = self.head
        prev = None
        while head.next is not None:
            prev = head
            head = head.next
        prev.next = None
        self.length -= 1

    def delete_from_specific_position(self, position):
        if position == 0:
            self.delete_at_beginning()
        elif position == self.length:
            self.delete_from_end()
        elif position > self.length:
            print(f"Position {position} is greater than length {self.length} of the LinkedList.")
        else:
            head = self.head
            prev = None
            count = 0
            while head is not None:
                prev = head
                head = head.next
                count += 1
                if position == count:
                    break

            prev.next = head.next


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    ll = LinkedList()
    ll.head = n1

    ll.traverse()

    # insert at beginning
    ll.insert_at_beginning(Node(0))
    ll.insert_at_beginning(Node(-1))
    ll.traverse()

    # insert at the end
    ll.insert_at_end(Node(6))
    ll.insert_at_end(Node(7))
    ll.traverse()

    # insert at position 2
    ll.insert_at_specific_position(Node(20), 2)
    ll.traverse()

    # insert at position 0
    ll.insert_at_specific_position(Node(10), 0)
    ll.traverse()

    # delete at the beginning
    ll.delete_at_beginning()
    ll.traverse()

    # delete from the end
    ll.delete_from_end()
    ll.traverse()

    # delete from position 2
    ll.delete_from_specific_position(2)
    ll.traverse()
