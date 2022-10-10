class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def search(self, root, data):
        if self.head is None or root is None:
            return False
        elif root.data == data:
            return True
        elif data < root.data:
            return self.search(root.left, data)
        elif data > root.data:
            return self.search(root.right, data)

    def insert(self, node):
        if node is None or self.head is None:
            return None

        current = self.head
        while node.data < current.data and current.left is not None:
            current = current.left

        if node.data < current.data:
            current.left = node
        else:
            current.right = node


if __name__ == "__main__":
    node10 = Node(10)
    bst = BinarySearchTree(node10)

    bst.insert(Node(8))
    bst.insert(Node(9))
    bst.insert(Node(6))
    bst.insert(Node(11))

    print(f"Found element: {bst.search(node10, 111)}")
