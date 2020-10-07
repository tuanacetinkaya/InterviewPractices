# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compl = []
        positions = [-1, -1]
        other = -1
        for i in range(len(nums)):
            complementary = target - nums[i]
            if nums[i] in compl:
                positions[1] = i
                other = complementary
                break
            else:
                compl.append(complementary)
        for j in range(len(nums)):
            if nums[j] == other:
                positions[0] = j
                return positions
        return

    def alternativeApproach(self, nums, target):
        if len(nums) <= 1:
            return False
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                return hmap[nums[i], i]
            hmap[target - nums[i]] = i


print(Solution().twoSum([3, 3], 6))

# Runtime: 384 ms, faster than 43.31% of Python online submissions for Two Sum.
# Memory Usage: 13.4 MB, less than 93.09% of Python online submissions for Two Sum.
# Time Submitted: 09/16/2020 02:16
