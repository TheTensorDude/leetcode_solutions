# Time: 
# Submission Link: https://leetcode.com/problems/merge-intervals/submissions/1232104486?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals with the first item
        intervals.sort(key = lambda x: x[0])
        
        out = [intervals[0]]
        for start, end in intervals[1:]:
            lastInterval = out[-1]
            if start <= lastInterval[-1]:
                # Check for the end bound as the items are
                # sorted by the first element
                endBound = max(end, lastInterval[-1])
                lastInterval[-1] = endBound
            else:
                out.append([
                    start,
                    end
                ])
        return out