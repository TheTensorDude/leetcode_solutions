# Time: O(n)
# Space: (n)
# Submission Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1230903654
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                added_val = stack.pop() + stack.pop()
                stack.append(added_val)
            elif c == '-':
                # The order matters
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif c == '*':
                mulled_val = stack.pop() * stack.pop()
                stack.append(mulled_val)
            elif c == '/':
                # The order matters
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                # The values are given as string so if it
                # is not an operator we need to convert it
                # back to integer
                stack.append(int(c))
        return stack[0]
