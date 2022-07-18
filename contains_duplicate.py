## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Input: nums = [1,2,3,1]
## Output: true

## Input: nums = [1,2,3,4]
## Output: false



## Optimal solution

def containsDuplicate(self, nums: List[int]) -> bool:
    if len(nums) ==  len(set(nums)):
        return False
    else:
        return True

        
        
        
## Not so optimal 

def containsDuplicate(self, nums: List[int]) -> bool:
    nums1 = []
    for i in range(len(nums)):
        nums1 = nums
        new_nums = list(set(nums1))
        if len(nums) > len(new_nums):
            return True
        else:
            return False
          
 ## lessons learnt: use len and set for duplicates and compare lens of original and set
