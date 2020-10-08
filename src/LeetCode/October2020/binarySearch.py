class Solution(object):

    def searchRecursive(self, nums, target):
        mid = len(nums) // 2
        while mid >= 0:
            if nums[mid] == target:
                return mid
            # if we're left with [0,3] and target = 2
            if mid < 1:
                return -1
            elif target > nums[mid]:
                val = self.searchRecursive(nums[mid:len(nums)], target)
                if not val or val == -1:
                    return -1
                return mid + val
            # target < nums[mid]
            return self.searchRecursive(nums[0:mid], target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchRecursive(nums, target)


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(Solution().search(nums, target))
