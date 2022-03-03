from __future__ import annotations
from typing import Any
from uuid import uuid4
from collections import deque

class Node:
    def __init__(self, value: Any, left: Node = None, right: Node = None):
        self.node_id = str(uuid4())
        self.value: Any = value
        self.left: Node = left
        self.right: Node = right

    def add_left(self, value: Any) -> None:
        self.left = Node(value)

    def add_right(self, value) -> None:
        self.right = Node(value)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.visited = {}
        self.root = root

    def dfs_recursive(self, value: Any) -> Node:
        real_root = self.root
        return self.__do_dfs(value, real_root)

    def __do_dfs(self, value, root: Node) -> Node:
        if root is None:
            return root

        self.visited[root.node_id] = root

        print(f'> value: {root.value}')
        if value == root.value:
            return root

        left = self.__do_dfs(value, root.left)
        right = self.__do_dfs(value, root.right)

        if left is not None:
            return left
        return right

    def dfs_iterative(self, value: Any) -> Node:
        stack = []
        stack.append(self.root)
        while(len(stack) > 0):
            node = stack.pop()
            print(f'>> {node.value}')
            if node.value == value:
                return node

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return None

    def bfs(self, value: Any) -> None:
        queue = deque()
        queue.append(self.root)
        while(len(queue) > 0):
            node = queue.popleft()
            print(f'>> {node.value}')
            if node.value == value:
                return node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    root = Node(value=1)
    root.left = Node(value=2)
    root.right = Node(value=3)
    root.left.left = Node(value=4)
    root.left.right = Node(value=5)

    btree = BinaryTree(root=root)
    node = btree.dfs_recursive(value=5)
    print(f'Found node with dfs recursive: {node}, value: {node.value}')

    btree = BinaryTree(root=root)
    node = btree.dfs_iterative(value=5)
    print(f'Found node with dfs iterative: {node}, value: {node.value}')

    btree = BinaryTree(root=root)
    node = btree.bfs(value=5)
    print(f'Found node with bfs: {node}, value: {node.value}')
