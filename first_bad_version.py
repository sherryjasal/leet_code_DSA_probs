## You are a product manager and currently leading a team to develop a new product. 
## Unfortunately, the latest version of your product fails the quality check. 
## Since each version is developed based on the previous version, all the versions after a bad version are also bad.

## Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

## You are given an API bool isBadVersion(version) which returns whether version is bad. 
## Implement a function to find the first bad version. You should minimize the number of calls to the API.


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0,n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
                
        return left
               
      
## lessons learnt
## it will be array of 0s and 1s i.e. [0,0,0,0,1,1,1,1,1]
## take mid of the array - use binary search. 
## as it is a sorted array so it will be 0s and 1s
        
