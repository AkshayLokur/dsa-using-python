class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, head):
        self.head = head

    def pre_order_traversal(self, node):
        print(node.data, end=" ")

        if node.left is not None:
            self.pre_order_traversal(node.left)

        if node.right is not None:
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node.left is not None:
            self.in_order_traversal(node.left)

        print(node.data, end=" ")

        if node.right is not None:
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node.left is not None:
            self.post_order_traversal(node.left)

        if node.right is not None:
            self.post_order_traversal(node.right)

        print(node.data, end=" ")


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.left = node2
    node2.left = node3
    node2.right = node4

    node1.right = node5
    node5.right = node6

    tree = Tree(node1)

    print("\nPre Order Traversal: ")
    tree.pre_order_traversal(node1)

    print("\nIn Order Traversal: ")
    tree.in_order_traversal(node1)

    print("\nPost Order Traversal: ")
    tree.post_order_traversal(node1)
