## Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## A subarray is a contiguous part of an array.


def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    min_sum = sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        max_sum = max(max_sum, sum - min_sum)
        min_sum = min(min_sum, sum)

    return max_sum
  
  ## lessons learnt: max_sum and min_sum and counter for sum of array 
