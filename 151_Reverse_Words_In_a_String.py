class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        left = 0
        ans = words[:]
        for right in range(len(words) - 1, -1, -1):
            ans[left] = words[right]
            left += 1

        return ' '.join(ans)