class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        left = 0
        running_sum = 0
        n = len(code)
        original = code[:]   # keep original unchanged

        for i in range(n):
            running_sum = 0
            if k > 0:
                for j in range(1, k+1):
                    running_sum += original[(i + j) % n]
            elif k < 0:
                for j in range(1, -k+1):
                    running_sum += original[(i - j) % n]
            else:
                running_sum = 0

            code[i] = running_sum
            running_sum = 0
            left += 1

        return code