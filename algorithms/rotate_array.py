# Time: O(n)
# Space: O(n)
# Submission Link: https://leetcode.com/problems/rotate-array/submissions/1226616861?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Trick: K can be greater than the length(n) of theb array
        # in this case, we can take k % n as if we rotate the array
        # n times we get back from where we started
        size = len(nums)
        k = k % size 
        # Swap
        left_chunk = nums[:size - k]
        nums[:k] = nums[size - k:]
        nums[k:] = left_chunk