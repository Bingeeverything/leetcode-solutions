class Solution:
    def isPalindrome(self, x: int) -> bool:
        yo = []
        for i in str(x):
            yo.append(i)
        return  yo[:] == yo[::-1]