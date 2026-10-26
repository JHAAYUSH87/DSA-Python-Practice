
# LeetCode 24: Swap Nodes in Pairs
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next


def to_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2], [2, 1])
    ]

    for values, expected in test_cases:
        head = to_linked_list(values)
        result = to_list(solution.swapPairs(head))

        print(
            f"Input: {values} | Output: {result} "
            f"| Passed: {result == expected}"
        )
