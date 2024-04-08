# Time: O((m+n)log(m+n))
# space: O(1)
# Submission Link: https://leetcode.com/problems/merge-sorted-array/submissions/1226042917?envType=study-plan-v2&envId=top-interview-150

class SolutionOne:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort() 
        for num in nums2:
            nums1[m] = num
            m += 1
        nums1.sort()
        


        


