class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        right = 0
        left = 0
        new = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                new.append(nums1[left])
                left += 1
            else:
                new.append(nums2[right])
                right += 1
        else:
            if left < len(nums1):
                while left < len(nums1):
                    new.append(nums1[left])
                    left += 1
            else:
                if right < len(nums2):
                    while right < len(nums2):
                        new.append(nums2[right])
                        right += 1
        n  =  len(new)

        if n % 2 != 0:
            median = new[n // 2]

        else:
            mid1 = new[n // 2- 1]
            mid2 = new[n // 2]
            median = (mid1 + mid2) / 2
        
        return median