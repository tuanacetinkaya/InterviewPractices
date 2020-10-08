# Done in about an hour: 08.10.2020

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        indx = self
        string = ""
        while indx:
            string = string + " " + str(indx.val)
            indx = indx.next
        return string


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        # measure the size of the list for efficiency
        current = head
        length = 1
        while current.next:
            length += 1
            current = current.next
        # created circular linkedlist
        current.next = head
        # avoid multiple tours along the list
        k = k % length

        current = head
        before = None
        for i in range(length - k):
            before = current
            current = current.next

        before.next = None

        return current


list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)

print(Solution().rotateRight(list, 2))
