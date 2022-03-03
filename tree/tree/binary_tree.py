from __future__ import annotations
from collections import deque
from typing import List

from tree.tree_node import TreeNode


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    @classmethod
    def generate(cls, numbers: List[int]) -> BinaryTree:
        binary_tree = BinaryTree()

        for number in numbers:
            binary_tree.add(number)

        return binary_tree

    def add(self, value: int):
        queue = deque()

        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.popleft()

            if current_node is None:
                self.root = TreeNode(value)
                break
            else:
                new_node = TreeNode(value)

            if current_node.left is None:
                current_node.left = new_node
                break
            else:
                queue.append(current_node.left)

            if current_node.right is None:
                current_node.right = new_node
                break
            else:
                queue.append(current_node.right)

    def display(self):
        current_node = self.root
        queue = deque()
        queue.append(current_node)

        result = deque()
        while len(queue) > 0:
            node: TreeNode = queue.popleft()

            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        print(list(result))
