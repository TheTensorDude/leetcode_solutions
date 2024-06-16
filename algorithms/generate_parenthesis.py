class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Base condition: open_count == close_count == n
        # If open_count > close_count then insert close
        # else if open_count < n then insert open

        stack = []
        out = []

        def backtrack(open_count, close_count, n):
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count, n)
                stack.pop()

            if open_count > close_count:
                stack.append(")")
                backtrack(open_count, close_count + 1, n)
                stack.pop()

            if open_count == close_count == n:
                out.append("".join(stack))
                return out

        backtrack(0, 0, n)
        return out