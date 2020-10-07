# 16.09.2020 -> Solved about 10 min
# Google:
#
# There are n people lined up, and each have a height represented as an integer.
# A murder has happened right in front of them, and only people who are taller than everyone in front of them
# are able to see what has happened. How many witnesses are there?
#
# Example:
# Input: [3, 6, 3, 4, 1]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.
#  #
#  #
#  # #
# ####
# ####
# #####
# 36341                                 x (murder scene)


def witnesses(heights):
    witness = 0
    tallest = 0
    for i in range(len(heights)):
        if heights[len(heights) - i - 1] > tallest:
            witness += 1
            tallest = heights[len(heights) - i - 1]
    return witness



print(witnesses([3, 6, 5, 8, 10]))
# 3
