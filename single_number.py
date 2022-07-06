## Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

##You must implement a solution with a linear runtime complexity and use only constant extra space.
## Input: nums = [2,2,1]
##Output: 1
## Input: nums = [4,1,2,1,2]
## Output: 4
## Input: nums = [1]
## Output: 1


  def singleNumber(self, nums: List[int]) -> int:
      result = 0
      for i in range(len(nums)):
          result = result ^ nums[i]
      return result

## The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts. 
##a) XOR of a number with itself is 0. 
##b) XOR of a number with 0 is number itself.

## res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

##Since XOR is associative and commutative, above 
##expression can be written as:
##res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
##    = 7 ^ 0 ^ 0 ^ 0
##    = 7 ^ 0
##    = 7 
