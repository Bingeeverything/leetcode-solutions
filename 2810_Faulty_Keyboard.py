class Solution:
    def finalString(self, s: str) -> str:
        new_string = []
        for string in s:
            if string != 'i':
                new_string.append(string)
            else:
                left = 0
                right = len(new_string) - 1
                while left < right:
                    new_string[left], new_string[right] = new_string[right],new_string[left]
                    left += 1
                    right -= 1
                    continue
        return ''.join(new_string)