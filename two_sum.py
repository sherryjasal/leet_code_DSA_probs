## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

## Input: nums = [2,7,11,15], target = 9
## Output: [0,1]
## Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


### Brute-Force Solution ###

##So, if we fix one of the numbers, say
## x
##, we have to scan the entire array to find the next number
## y
## which is
## value - x
## where value is the input parameter. Can we change our array somehow so that this search becomes faster?

  def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
          for j in range(i+1, len(nums)):
              if nums[j] == target - nums[i]:
                  return [i, j]
                
 ## It takes O(n^2)

### The other method is to use hashmaps for time and space complexity as it is O(1)

##A simple implementation uses two iterations. In the first iteration, we add each element's value as a key and its index as a value to the hash table. Then, in the second iteration, we check if each element's complement (
##target-nums[i] target−nums[i]) exists in the hash table. If it does exist, we return current element's index and its complement's index. Beware that the complement must not be 
##nums[i] itself!

## fast lookup

##  reduce the lookup time from 
##  O(n) to O(1). O(1) by trading space for speed.

  def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmap = {}
      for i in range(len(nums)):
          hashmap[nums[i]] = i
          for i in range(len(nums)):
              compliment = target - nums[i]
              if compliment in hashmap and hashmap[compliment] != i:
                  return [i, hashmap[compliment]]
