class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return

            remaining = k - len(path)


            min_sum = sum(range(start, start + remaining))
            max_sum = sum(range(9, 9 - remaining, -1))

            if total + min_sum > n or total + max_sum < n:
                return

            for i in range(start, 10):
                backtrack(i + 1, path + [i], total + i)

        backtrack(1, [], 0)
        return res
