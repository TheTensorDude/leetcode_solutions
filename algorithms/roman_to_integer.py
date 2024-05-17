# Kinda the noob way!
class Solution:
    def romanToInt(self, s: str) -> int:
        cache = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        current = 0
        size = len(s)
        out = 0
        while current < size:
            currItem = s[current]
            if current + 1 == size:
                out += cache[currItem]
                return out
            nextItem = s[current + 1]
            if currItem == "I" and nextItem in ["V", "X"]:
                out += cache[nextItem] - cache[currItem]
                current += 2
            elif currItem == "X" and nextItem in ["L", "C"]:
                out += cache[nextItem] - cache[currItem]
                current += 2
            elif currItem == "C" and nextItem in ["D", "M"]:
                out += cache[nextItem] - cache[currItem]
                current += 2
            else:
                out += cache[currItem]
                current += 1
        return out
    
# But the input is sorted?
# Can not we just reduce the value if the value(next) > value(current)
class Solution:
    def romanToInt(self, s: str) -> int:
        cache = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
        current = 0
        size = len(s)
        out = 0
        while current < size:
            if current + 1 < size and cache[s[current]] < cache[s[current + 1]]:
                out += cache[s[current + 1]] - cache[s[current]]
                current += 2
            else:
                out += cache[s[current]]
                current += 1
        return out