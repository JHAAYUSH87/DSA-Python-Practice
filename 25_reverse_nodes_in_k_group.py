
# LeetCode 25: Reverse Nodes in k-Group
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp


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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([], 2, []),
        ([1], 2, [1]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1])
    ]

    for values, k, expected in test_cases:
        head = to_linked_list(values)
        result = to_list(solution.reverseKGroup(head, k))

        print(
            f"Input: {values}, k={k} | Output: {result} "
            f"| Passed: {result == expected}"
        )
