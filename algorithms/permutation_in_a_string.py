class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortedString = sorted(s1)
        window_size = len(s1)
        length = len(s2)
        for i in range(length - window_size + 1):
            isAnagram = sortedString == sorted(s2[i : i + window_size])
            if isAnagram:
                return True
        return False
