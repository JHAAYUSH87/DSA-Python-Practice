
# LeetCode 19: Remove Nth Node From End of List
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test Case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.removeNthFromEnd(head, 2)

print("Output:", print_list(result))
