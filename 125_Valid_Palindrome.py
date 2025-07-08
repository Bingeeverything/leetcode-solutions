class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        c = re.sub(r'[^A-Za-z0-9]','', s)
        return c == c[::-1]