## Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

##Specifically, ans is the concatenation of two nums arrays.

## Return the array ans.

## Input: nums = [1,2,1]
## Output: [1,2,1,1,2,1]
## Explanation: The array ans is formed as follows:
## - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
## - ans = [1,2,1,1,2,1]

## Input: nums = [1,3,2,1]
## Output: [1,3,2,1,1,3,2,1]
## Explanation: The array ans is formed as follows:
## - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
## - ans = [1,3,2,1,1,3,2,1]



def getConcatenation(self, nums: List[int]) -> List[int]:
    nums == nums
    ans = nums + nums
    return ans
    
 ##Another approach:     
def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            ans = nums
            ans.append(nums[i])
        return ans
    
 ## lessons learnt: use append or + only with lists i.e. nums an not with nums[i] - otherwise it will treat this as an integer
## you can only append elements in the list
