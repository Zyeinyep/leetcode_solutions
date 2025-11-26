class Solution:
    # Logic: use stack; push opens, pop on matching closes.
    # Time: O(n)
    # Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:                 # closing bracket
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()             # valid match
                else:
                    return False            # mismatch
            else:
                stack.append(ch)            # opening bracket

        return len(stack) == 0
