from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        yo = Counter(nums).most_common(1)  
        return yo[0][0] 