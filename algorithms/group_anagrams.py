# Time: O(nmlog(m))
# Space: O(nm)
# Submission Link: https://leetcode.com/problems/group-anagrams/submissions/1228420140?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict()
        for string in strs:
            key = ''.join(sorted(string))
            if key in cache:
                cache[key].append(string)
            else:
                cache[key] = [string]
        return list(cache.values())