class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        my_set = set()
        while True:
            my_set.add(n)
            count = 0
            while n != 0:
                digit = n%10
                count += digit * digit
                n = n// 10
            n =count  
            if n in my_set:
                return False
            if n == 1:
                return True         