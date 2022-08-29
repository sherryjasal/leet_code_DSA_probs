## Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

## Return the running sum of nums.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_array = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result_array.append(total)
        return result_array
      
## lessons learnt for count or sum use a counter approach and then append elts
