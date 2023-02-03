## Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
## If target exists, then return its index. Otherwise, return -1.
## You must write an algorithm with O(log n) runtime complexity.
## Input: nums = [-1,0,3,5,9,12], target = 9
## Output: 4
## Explanation: 9 exists in nums and its index is 4

##Input: nums = [-1,0,3,5,9,12], target = 2
## Output: -1
## Explanation: 2 does not exist in nums so return -1


##Constraints:

##1 <= nums.length <= 104
##-104 < nums[i], target < 104
##All the integers in nums are unique.
##nums is sorted in ascending order.

def search(self, nums: List[int], target: int) -> int:
    initial = 0
    end = len(nums)

    while initial < end:
        mid = ((end-initial)//2)+initial
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            initial = mid+1

    return -1
  
## Though this is not an optimised solution but it is using binary search
## since it sorted so in binary search left will always be lesser than right and compare it with mid elt


def binarysearch(self, arr, n, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i

    return -1
