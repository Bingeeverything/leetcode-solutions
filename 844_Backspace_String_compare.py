class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def conver(s):
            stack1 = []
            for i in s:
                if i == '#':
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(i)
            return ''.join(stack1)
        return conver(s) == conver(t)