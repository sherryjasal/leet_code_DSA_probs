## You are climbing a staircase. It takes n steps to reach the top.

## Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1 #initialize 1,1 for the end array
        for i in range(n-1):
            temp = one # store one in temp
            one = one + two # update one
            two = temp #then update two as it goes backwards
        return one 
      
## lessons learnt
