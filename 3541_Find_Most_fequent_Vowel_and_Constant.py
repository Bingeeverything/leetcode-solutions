class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}
        vowel_set = {'a', 'e', 'i', 'o', 'u'}

        for char in s:
            if char in vowel_set:
                vowels[char] = vowels.get(char, 0) + 1
            else:
                consonants[char] = consonants.get(char, 0) + 1

        max_vowel = max(vowels.values()) if vowels else 0
        max_consonant = max(consonants.values()) if consonants else 0
        
        return max_vowel + max_consonant