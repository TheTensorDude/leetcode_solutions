# Time: O(n^2)
# Space: O(1)
# Submission Link: TLE
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = []
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    out.append(nums[i])
        return out
    
# -------------- More optimised -------------
# Time: O(n)
# Space: O(n)
# Submission Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1226663865
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
                continue
            out.append(num)
        return out
    
# ------------ Expected Solution -------------
# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1227267737
# Trick: Use the given array as extra memory. We can make the element -ve
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        for i, num in enumerate(nums):
            map_index = abs(num) - 1
            value = nums[map_index]
            if value < 0:
                out.append(abs(num))
                continue
            nums[map_index] = -nums[map_index]
        return out