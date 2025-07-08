class Solution(object):
    def intersection(self, nums1, nums2):
        hmm = []
        for i in nums1:
            if i in hmm:
                continue
            if i in nums2:
                hmm.append(i)
        return hmm