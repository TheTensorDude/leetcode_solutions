# Time: O(n)
# Space: O(1)
# Submission Link: https://leetcode.com/problems/factorial-trailing-zeroes/submissions/1229522852?envType=study-plan-v2&envId=top-interview-150
# TODO: Read https://www.purplemath.com/modules/factzero.htm
# TODO: Implement the solution efficiently
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        for i in range(1, n + 1):
            fact *= i

        count = 0
        while not bool(fact % 10):
            count += 1
            fact //= 10

        return count
    