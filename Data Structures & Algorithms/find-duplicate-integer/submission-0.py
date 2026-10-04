class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}

        nums
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return nums[i]
