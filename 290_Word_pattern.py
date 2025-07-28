class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        if len(ss) != len(pattern):
            return False
        has = {}
        has2 = {}
        for c,w in zip(pattern, ss):
            if c in has:
                if has[c] != w:
                    return False
            else:
                has[c] = w
            if w in has2:
                if has2[w] != c:
                    return False
            else:
                has2[w] = c
        return True