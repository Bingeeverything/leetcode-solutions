class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ''
        ans = ''
        found = False
        
        for i in word:
            if not found:
                res += i
                if i == ch:
                    found = True
                    ans += res[::-1]
            else:
                ans += i
        
        if not found:
            return word
        
        return ans