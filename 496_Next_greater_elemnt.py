class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mydic = {}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop
                if stack:
                    mydic[num] = stack[-1]
                else:
                    mydic[num] = -1
                stack.append(num)
            stack.append(mydic[num])
        return stack                