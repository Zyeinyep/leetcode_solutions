from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i,e in enumerate(nums):
            freq[e] += 1
        sorted_keys = dict(sorted(freq.items(), key=lambda x: x[1]))
       
        curr = list(sorted_keys.keys())
        return curr[-k:]


        
