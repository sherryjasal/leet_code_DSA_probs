## Given a string s, find the length of the longest substring without repeating characters.

## Input: s = "abcabcbb"
## Output: 3
## Explanation: The answer is "abc", with the length of 3.

## Input: s = "pwwkew"
## Output: 3

  def lengthOfLongestSubstring(self, s: str) -> int:
      max_len = 1
      if s == '':
          return 0
      for i in range(len(s)):
          substring = s[i]
          for j in range(i+1, len(s)):
              if s[j] not in substring:
                  substring = substring + s[j]
                  max_len = max(max_len, len(substring))
              else:
                  break

      return max_len
    
 ## Not an optimal approach: as it is two loops O(N^2) 
## lessons learnt: not in - while creating new array
