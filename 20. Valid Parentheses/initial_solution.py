class Solution:
    # Logic: push opens; pop when matching close appears.
    # Time: O(n)
    # Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    continue
            elif i == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                    continue
            elif i == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                    continue

            stack.append(i)

        if len(stack) == 0:
            return True
        return False
