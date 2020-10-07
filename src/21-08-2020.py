#Todo 31.08.2020 (Failed)
# Microsoft:
#
# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self.val


class Solution:

    def add_two_numbers(self, l1, l2, c=0):
        solution = ListNode(0)
        addition = l1.val + l2.val + c
        division, remainder = divmod(addition, 10)

        if not (l1.next and l2.next and c):
            return ListNode(remainder)

        solution.next = self.add_two_numbers(l1.next, l2.next, division)

    # steps
    # 1 7 8
    # 9 5 5
    # 10 12 13
    # 1 0 12 13
    # 1 1 2 13
    # 1 1 3 3


l1 = ListNode(7)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().add_two_numbers(l1, l2)
while result:
    print(result.val),
    result = result.next
# 7 0 8
