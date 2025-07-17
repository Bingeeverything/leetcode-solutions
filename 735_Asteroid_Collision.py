class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while alive and i  < 0 and stack and stack[-1] > 0:
                if stack[-1] == abs(i):
                    stack.pop()
                    alive = False
                elif stack[-1] > abs(i):
                    alive = False
                elif stack[-1] < abs(i):
                    stack.pop()
            if alive:
                stack.append(i)
        return stack    