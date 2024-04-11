class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) // 2
            if  nums[mid - 1] <  nums[mid] < nums[mid + 1]:
                low += 1
            elif nums[mid - 1] >  nums[mid] > nums[mid + 1]:
                high -= 1
            else: 
                return mid 
            
            
                