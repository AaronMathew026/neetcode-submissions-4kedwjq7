class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}


        for paran in s:
            if paran in pairs.values():
                stack.append(paran)
            elif paran in pairs:
                if not stack:
                    return False
                if stack[-1] == pairs[paran]:
                    stack.pop()
                else:
                    return False

        return not stack

            