## Given an integer n, return true if it is a power of two. Otherwise, return false.

## An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            n /= 2
        return n == 1
      
## lessons learnt: think of 3 scenarios negative, 0, and positive conditions
