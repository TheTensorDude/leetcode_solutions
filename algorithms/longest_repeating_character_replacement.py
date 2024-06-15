class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        count = Counter()
        left, right = 0, 0
        max_count = 0
        res = 0

        while right < size:
            # Include the character at the right pointer into the count
            count[s[right]] += 1
            # Update the count of the most frequent character in the current window
            max_count = max(max_count, count[s[right]])

            # Calculate the window size
            window_size = right - left + 1

            # If the number of characters to replace is more than k, shrink the window
            if window_size - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update the result with the maximum length of the window that meets the criteria
            res = max(res, right - left + 1)

            # Move the right pointer to expand the window
            right += 1

        return res
