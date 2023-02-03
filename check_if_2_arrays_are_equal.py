#Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
#Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

## Input:
##N = 5
##A[] = {1,2,5,4,0}
##B[] = {2,4,5,0,1}
##Output: 1
##Explanation: Both the array can be 
##rearranged to {0,1,2,4,5}

##Input:
##N = 3
##A[] = {1,2,5}
##B[] = {2,4,15}
##Output: 0
##Explanation: A[] and B[] have only one common value.


class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        if sorted(A) == sorted(B):
            return 1
        else:
            return 0
          
## Lessons Learnt
## sort() sorts the list and replaces the original list, whereas sorted(list) returns a sorted copy of the list, without changing the original list.
