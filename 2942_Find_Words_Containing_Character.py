class Solution(object):
    def findWordsContaining(self, words, x):
        out = []
        for i,w in enumerate(words):
                if x in w:
                    out.append(i)
        return out
        