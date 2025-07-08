from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [c for c, _ in Counter(nums).most_common(k)]
        return counts
