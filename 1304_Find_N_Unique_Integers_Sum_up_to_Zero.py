class Solution:
    def sumZero(self, n: int) -> List[int]:
        stack = []
        number = 1
        if n % 2 == 0:
            while len(stack) != n:
                stack.append(number)
                stack.append(- number)
                number += 1
        else:
            while len(stack) != n - 1:
                stack.append(number)
                stack.append(- number)
                number += 1
        if n % 2 != 0:
            stack.append(0)
        return stack