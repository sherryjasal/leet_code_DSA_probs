## A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

## Given a string s, return true if it is a palindrome, or false otherwise.


## Approach 1 : Using List Comprehension
def isPalindrome(self, s: str) -> bool:
    new_str = [char.lower() for char in s if char.isalnum()]
    return new_str == new_str[::-1]
    
## Approach 2: Using Loop

  def isPalindrome(self, s: str) -> bool:
      new_str = ''

      for char in s:
          if char.isalnum():
              new_str += char.lower()

      return new_str == new_str[::-1]
    
## lessons learnt 
## isalnum is bool  checks for if all string has char and nums ,
## using list comprehension will take less time but more space
## loop will take more time and less space
