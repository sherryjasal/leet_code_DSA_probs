## You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

## Return the length of the longest substring containing the same letter you can get after performing the above operations.



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0 # sliding window = r-l+1 , #max frequency of the element occuring in hashmap, max(counter.values())       
        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r],0) #if there is value on the right pointer return that else 0
            while (r-l+1)-max(counter.values()) > k:
                counter[s[l]] -= 1     # until sliding value - max frequesncy of element is greater than k else reduce the counter of left pointer by 1
                                       
                l += 1                 # else increase the counter by 1
            
             res = max(res, r-l+1)     # result is maximum of result and sliding window
        return res 
      
## lessons learnt:
## hashmaps, sliding window 
## sliding window use left right pointer 
