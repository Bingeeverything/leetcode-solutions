class Solution:
    def reverse(self, x: int) -> int:
        number1 = ''
        number2 = '-'
        yes = False

        for i in reversed(str(x)):
            if i == '-':
                yes = True
            else:
                number1 += i
        
        if yes == True:
            final_number = number2 + number1 
        else:
            final_number = number1 
        
        result = int(final_number)
        
        if result > 2**31 - 1 or result < -2**31:
            return 0
        else:
            return result