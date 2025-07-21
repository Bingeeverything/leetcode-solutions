class Solution:
    def makeFancyString(self, s: str) -> str:
        yo = []
        count = 1  # Start with 1 because we always take the first character

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                yo.append(s[i])
        return ''.join(yo)
