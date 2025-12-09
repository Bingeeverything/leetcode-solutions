class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = nums[n:]
        nums1 = nums[:n]
        ans = []

        for i in range(n):
            ans.append(nums1[i])
            ans.append(nums2[i])

        return ans