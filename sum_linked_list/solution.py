from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self):
        print("value", self.val)
        print("next", self.next)
        print("==================")


class LinkedList:
    @classmethod
    def generate(cls, lst: List[int]) -> ListNode:

        root = None
        current = None

        for num in lst:
            new_node = ListNode(val=num)

            if root is None:
                root = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next

        return root

    @classmethod
    def display(cls, root: ListNode):
        root.display()

        if root.next is None:
            return

        cls.display(root=root.next)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = self.num_in_linked_list(l1)
        second = self.num_in_linked_list(l2)

        sum = first + second

        sum_str = str(sum)[::-1]  # reversed

        print(first)
        print(second)
        print(sum)

        return LinkedList.generate([int(num_str) for num_str in sum_str])

    def num_in_linked_list(self, lst: Optional[ListNode]) -> int:
        if lst.next == None:
            return lst.val

        num_str = ""
        current = lst

        while current is not None:
            num_str += str(current.val)
            current = current.next

        return int(num_str[::-1])


if __name__ == "__main__":
    first = LinkedList.generate([1, 2, 3])
    second = LinkedList.generate([5, 2, 4])

    s = Solution()
    result = s.addTwoNumbers(first, second)

    LinkedList.display(result)
