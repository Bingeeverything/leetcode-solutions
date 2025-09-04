class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        stack = []
        for i in order:
            if i in friends:
                stack.append(i)
            else:
                pass
        return stack