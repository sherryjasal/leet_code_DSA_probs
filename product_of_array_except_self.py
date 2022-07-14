## Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

## The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## You must write an algorithm that runs in O(n) time and without using the division operation.



def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    for i in range(len(nums)):
        left = 1
        right = 1
        for j in range(0, i):
            left *= nums[j]
        for k in range(i+1, len(nums)):
            right *= nums[k]
        answer.append(left*right)
    return answer
  
  
  ## lessons learnt:  find the product of all the numbers to its left, find the product of all the numbers to its right, and the product of these two numbers is the answer
