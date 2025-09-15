class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        new_word = []
        if len(words) == 0:
            return 0
        for i in words:
            if not any(j in i for j in brokenLetters):
                new_word.append(i)
        return len(new_word)