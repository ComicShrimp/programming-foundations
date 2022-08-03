from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.left_node = None
        self.right_node = None
        self.data = data

    def add(self, data: Any) -> None:
        if self.left_node:
            self.add_right(Node(data))
        else:
            self.add_left(Node(data))

    def add_right(self, node) -> None:
        self.right_node = node

    def add_left(self, node) -> None:
        self.left_node = node


def print_tree(node: Node) -> str:
    if node:
        return f"< {node.data} {print_tree(node.left_node)} {print_tree(node.right_node)} >"
    else:
        return "<>"


# Main Code

root = Node(1)
root.add(2)
root.add(3)

print(print_tree(root))
