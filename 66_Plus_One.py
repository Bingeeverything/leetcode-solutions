class Solution(object):
    def plusOne(self, digits):
        add = ''
        yo = []
        for i in digits:
            add += str(i)
        added = int(add) + 1
        added_str = str(added)
        for i in added_str:
            yo.append(int(i))
        return yo