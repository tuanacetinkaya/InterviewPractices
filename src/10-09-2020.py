#Todo iterative version
# Microsoft:
#
# You 2 integers n and m representing an n by m grid, determine the number of ways you can get
# from the top-left to the bottom-right of the matrix y going only right or down.
#
# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.
import numpy as np

def num_ways_recursive(n, m):
    if m == 1 or n == 1:
        return 1
    return num_ways_recursive(n-1, m) + num_ways_recursive(n, m-1)


print(num_ways_recursive(55, 71))
# 2
