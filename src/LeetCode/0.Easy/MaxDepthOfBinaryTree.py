#
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        return self.searchBT(root, level)

    def searchBT(self, root, level):

        visited = {}

        if not root:
            return 1

        if not visited[root]:
            visited[root] = level
        if root.left:
            maxLeft = self.searchBT(self, root.left, level + 1)
        if root.right:
            maxRight = self.searchBT(self, root.right, level + 1)
        return max(maxLeft, maxRight)


t2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))
print(Solution().maxDepth(t2))
