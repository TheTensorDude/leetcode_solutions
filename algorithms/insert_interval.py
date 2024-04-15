class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Intervals is sorted in ascending order
        # Use binary search to find it's relevant position
        size = len(intervals)
        low, high = 0, size - 1
        target = newInterval[0]
        INSERTED = False
        while low <= high:
            mid = (low + high) // 2
            currentInterval = intervals[mid]
            if currentInterval[0] < target:
                low += 1
            elif currentInterval[0] > target:
                high -= 1
            else:
                matched = intervals[mid]
                intervals[mid] = [target, max(matched[-1], newInterval[-1])]
                INSERTED = True
                break

        # desired position
        if not INSERTED:
            intervals.insert(low, newInterval)

        # Remember that intervals is still sorted
        out = [intervals[0]]
        for start, end in intervals[1:]:
            lastInterval = out[-1]
            if start <= lastInterval[-1]:
                endBound = max(lastInterval[-1], end)
                lastInterval[-1] = endBound
            else:
                out.append(
                    [
                        start,
                        end
                    ]
                )
        return out
