# you have given a binary tree
# return if this tree is a valid binary tree
# with all nodes on the left is smaller than the parent
#  and all nodes on the right is greater
# 02.09.2020 -> TechLead CoderPro free overview questions
from math import inf


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# I couldn't come up with a solution for this one so the Solution class belongs to TechLead
class Solution:

    def bounded(self, low, node, high):
        if not node:
            return True
        if (low < node.val < high) and \
                self.bounded(low, node.left, node.val) and \
                self.bounded(node.val, node.right, high):
            return True
        return False

    def isValid(self, top_node):
        return self.bounded((-inf), top_node, inf)


#    5
#   / \
#  4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
# True

#    5
#   / \
#  4   7
#      /
#     2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
# False

print(Solution().isValid(node))
