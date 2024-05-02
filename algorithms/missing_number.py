class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        out = set(range(0, maxNum + 1)) - set(nums)
        return maxNum + 1 if not out else list(out)[0]


# Sum Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)
