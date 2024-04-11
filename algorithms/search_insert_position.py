# Time: O(logn)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/search-insert-position/submissions/1228399139?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low += 1
            elif nums[mid] > target:
                high -= 1
            else:
                return mid
        # low will always have the expected position of the target
        # and before the loop's condition breaks
        return low