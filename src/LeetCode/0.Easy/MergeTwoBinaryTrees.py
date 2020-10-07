# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        output = []
        # curr = self
        # while curr.left or curr.right:
        #     output.append(self.val)
        #     if self.left:
        #         output.append(self.left.val)
        #     if self.right:
        #         output.append(self.right.val)
        #     curr
        length = 3
        for i in range(1 + length):
            output.append(self)





class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        left1, left2, right1, right2 = (None, None, None, None)

        if not (t1 and t2):
            return
        if not t1:
            newVal = t2.val
            left2 = None
            right2 = None

        if not t2:
            newVal = t1.val,

            left1 = None
            right1 = None

        if t1 and t2:
            left1 = t1.left
            left2 = t2.left
            right1 = t1.right
            right2 = t2.right
            newVal = t1.val + t2.val

        mergedTree = TreeNode(newVal,
                              left=self.mergeTrees(left1, left2),
                              right=self.mergeTrees(right1, right2))
        return mergedTree

    # Example1:
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
# Note: The merging process must start from the root nodes of both trees.
# t1 -> [1,3,2,5]
# t2 -> [2,1,3,null,4,null,7]
t1 = TreeNode(1, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(2))
t2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))

print(Solution().mergeTrees(t1, t2))

