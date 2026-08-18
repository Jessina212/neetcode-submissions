class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        


        high = len(nums)
        low = 0

        while low <= high and low < len(nums):
            mid = (low + high)//2
            l = nums[mid]

            if l > target:
                high = mid - 1
            elif l < target:
                low = mid + 1
            else:
                return mid
        
        return -1