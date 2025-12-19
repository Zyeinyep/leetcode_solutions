class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        s = sorted(intervals, key=lambda x: (x[1], -x[0]))
        seen = []
        for i,e in enumerate(s):
            if len(seen) == 0:
                seen.append(e[-1]-1)
                seen.append(e[-1])
            else:
                count = 0
                for j in seen:
                    if  e[0] <= j <= e[1]:
                        count += 1
                if count >= 2:
                    continue
                else:
                    if count == 1:
                        seen.append(e[-1])
                    else:
                        seen.append(e[-1]-1)
                        seen.append(e[-1])
        return len(seen)

