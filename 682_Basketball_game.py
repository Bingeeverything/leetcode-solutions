class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif i == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)