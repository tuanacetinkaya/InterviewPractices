# 09.09.2020 -> Solved around 40 mins
# Amazon:
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous sub-array of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.


class Solution:

    def minSubArrayLen(self, nums, s):
        start, end = 0, 0
        sum = 0
        shortest = 0
        while start < len(nums):
            if sum < s:
                sum += nums[end]
                end += 1
            else:  # sum >= s
                subLength = end - start + 1
                if subLength < shortest:
                    shortest = subLength
                sum -= nums[start]
                start += 1
        return end - start + 1


array = [2, 3, 1, 2, 4, 3, 7]
print(Solution().minSubArrayLen(array, 7))
# 2
