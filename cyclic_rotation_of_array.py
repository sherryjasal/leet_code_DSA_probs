def rotate(self, nums: List[int], k: int) -> None:
    for i in range(k):
        rotateby1(nums)
 
def rotateby1(nums: List[int]):
    temp = arr[0]
    for i in range(0,n-1):
        a[i] = a[i+1]
    a[n-1] = temp
    
## lessons learnt: remove - shift - restore
## create temp initialised to position 0 - shifting in original array and temp will be arr[n-1]. Call the function rotationby1 for k 
