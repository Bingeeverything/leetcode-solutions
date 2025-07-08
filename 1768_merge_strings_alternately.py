class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)
        result.extend(word1[len(word2):])
        result.extend(word2[len(word1):])
        return ''.join(result)
