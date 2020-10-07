# Todo...
# Two images A and B are given, represented as binary, square matrices of the same size.
# (A binary matrix has only 0s and 1s as values.)
#
# We translate one image however we choose (sliding it left, right, up, or down any number of units),
# and place it on top of the other image.  After, the overlap of this translation is the number of positions
# that have a 1 in both images.
#
# (Note also that a translation does not include any kind of rotation.)
#
# What is the largest possible overlap?
#
# Example 1:
#
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes:
#
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1

class Solution(object):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: int
    """

    def getImage(self, A):
        image = {}
        for y in range(len(A)):
            for x in range(len(A[y])):
                if A[y, x]:
                    key = [x, y]
                    image[key] = True
        return image

    def getDistance(self, a_image):
        distance = []
        initial = a_image[0]

        # we skipped the first element since we implemented it
        for i in range(len(a_image))[1:]:
            diff = [initial[0] - a_image[i][0], initial[1] - a_image[i][1]]
            initial = a_image[i]
            distance.append(diff)
        return distance

    def largestOverlap(self, A, B):
        a_diff = self.getDistance(self.getImage(A))
        b_diff = self.getDistance(self.getImage(B))

        overlap = 0
        for pos in a_diff:
            if pos in b_diff:
                overlap += 1
        return overlap + 1


A = [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
B = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 1]]

print(Solution().largestOverlap(A, B))