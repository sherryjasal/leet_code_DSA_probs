## Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

##An input string is valid if:

##Open brackets must be closed by the same type of brackets.
##Open brackets must be closed in the correct order.


  def isValid(self, s: str) -> bool:
      stack = []
      for c in s:
          if c == "{":
              stack.append("}")
          elif c == "(":
              stack.append(")")
          elif c == "[":
              stack.append("]")
          elif not stack or stack.pop() != c:
              return False

      return not stack
    
    
  ## lesson learnt: stacks, appending the last element and adding the elements at the last. Also, if its not in stack or popped = c then its false
