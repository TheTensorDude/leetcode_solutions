class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1

        if x < 0:
            reversedInt = self.reverseInteger(-x)
            return -reversedInt if -reversedInt > MIN else 0
        else:
            reversedInt = self.reverseInteger(x)
            return reversedInt if reversedInt < MAX else 0

    def reverseInteger(self, number: int) -> int:
        out = 0
        while number > 0:
            last = number % 10
            out = (out * 10) + last
            number //= 10
        return out