
# LeetCode 21: Merge Two Sorted Lists
# Time Complexity: O(n + m)
# Auxiliary Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

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

    list1 = to_linked_list([1, 2, 4])
    list2 = to_linked_list([1, 3, 4])

    result = solution.mergeTwoLists(list1, list2)

    print("Output:", to_list(result))
    print("Expected:", [1, 1, 2, 3, 4, 4])
    print("Test passed:", to_list(result) == [1, 1, 2, 3, 4, 4])
