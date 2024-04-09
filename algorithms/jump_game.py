# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/jump-game/submissions/1227298132?envType=study-plan-v2&envId=top-interview-150
# Trick: Start from the end, update target is index + steps >= target
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(target - 1, -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0