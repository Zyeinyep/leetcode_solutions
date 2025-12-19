class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # p1 < p2 are the last two chosen numbers
        p1, p2 = -1, -1
        ans = 0

        for start, end in intervals:
            # Case 1: both points already cover the interval
            if start <= p1 and p2 <= end:
                continue

            # Case 2: only p2 is inside
            if start <= p2 <= end:
                ans += 1
                p1 = p2
                p2 = end

            # Case 3: none are inside
            else:
                ans += 2
                p1 = end - 1
                p2 = end

        return ans
