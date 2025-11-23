from typing import List

class Solution:
    # Checks if the last bit is a one-bit character.
    # Logic: Iterate through the bits from left to right.
    #        - If a '1' is found, skip the next bit (two-bit character).
    #        - If a '0' is found, move one step (one-bit character).
    #        - Stop before the last bit, then check if the last bit is standalone.
    # Runtime: O(n), each bit is visited at most once.
    # Space: O(1), no extra data structures are used.
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2  # skip two-bit character
            else:
                i += 1  # move past one-bit character
        return i == len(bits) - 1  # True if last bit is one-bit character
