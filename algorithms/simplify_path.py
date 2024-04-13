# Submission Link: https://leetcode.com/problems/simplify-path/submissions/1230965096?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def simplifyPath(self, path: str) -> str:
        modPath = []
        length = 0
        
        string = ''
        for char in path:
            if char != '/':
                string += char
            else:
                if string:
                    modPath.append(string)
                    length += 1
                string = ''
                modPath.append(char)
                length += 1
        if string:
            modPath.append(string)
            length += 1
        
        stack = []
        for i, item in enumerate(modPath):
            if item == '/':
                if stack and stack[-1] == '/':
                    continue
                else:
                    stack.append(item)

            elif item == '..':
                currLen = len(stack)
                if currLen > 2:
                    stack.pop()
                    stack.pop()
            elif item == '.':
                continue
            else:
                stack.append(item)
        out = ''.join(stack)
        return out[:-1] if out.endswith('/') and len(out) > 1 else out