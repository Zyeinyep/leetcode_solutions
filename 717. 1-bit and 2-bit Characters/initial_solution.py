# Checks if the last bit is a one-bit character.
# Uses a queue to track two-bit characters.
# Time: O(n), Space: O(1)

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        queue = []
        for i, e in enumerate(bits):
            if len(queue) == 0:
                if e == 1:
                    queue.append(1)
                elif i == len(bits) - 1:
                    return True
            else:
                queue.pop()
        return False
