class Solution:
    def largestGoodInteger(self, num: str) -> str:
        word = []
        yo = ''
        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                if len(yo) == 0:
                    yo += num[i - 1] + num[i]
                else:
                    yo += num[i]
            else:
                yo = ''
            if len(yo) == 3:
                word.append(yo)
                yo = ''
        if word:
            return max(word)
        else:
            return ''