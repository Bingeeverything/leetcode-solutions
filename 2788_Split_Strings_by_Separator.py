class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            ws = word.split(separator)
            ws = [w for w in ws if w]
            ans.extend(ws)
        return ans