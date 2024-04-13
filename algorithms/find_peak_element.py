# Time: o(logn)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/find-peak-element/submissions/1229326502?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) // 2

            # Edge case if we are out of bound then return mid
            if mid + 1 > high and mid - 1 < low:
                return mid

            if nums[mid + 1] > nums[mid]:
                low = mid + 1
            elif nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                return mid
                