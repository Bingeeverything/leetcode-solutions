from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Always count the smaller list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = Counter(nums1)
        yo = []

        for num in nums2:
            if count[num] > 0:
                yo.append(num)
                count[num] -= 1

        return yo
