class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [str(digit) for digit in str(num)]
        yo = []
        count = 0
        for i in nums:
            if count == 0 and i == '6':
                yo.append(9)
                count += 1
            else:
                yo.append(i)
        res = [str(digit) for digit in yo]
        return int(''.join(res))