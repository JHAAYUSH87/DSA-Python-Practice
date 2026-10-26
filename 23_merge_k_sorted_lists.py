
# LeetCode 23: Merge k Sorted Lists
# Time Complexity: O(N log k)
# Auxiliary Space: O(k)

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            _, i, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(
                    min_heap, (node.next.val, i, node.next)
                )

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

    lists = [
        to_linked_list([1, 4, 5]),
        to_linked_list([1, 3, 4]),
        to_linked_list([2, 6])
    ]

    result = solution.mergeKLists(lists)
    output = to_list(result)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]

    print("Output:", output)
    print("Expected:", expected)
    print("Test passed:", output == expected)
