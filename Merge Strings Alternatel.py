#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

#Input: word1 = "abc", word2 = "pqr"
#Output: "apbqcr"
#Explanation: The merged string will be merged as so:
#word1:  a   b   c
#word2:    p   q   r
#merged: a p b q c r

#Input: word1 = "ab", word2 = "pqrs"
#Output: "apbqrs"
#Explanation: Notice that as word2 is longer, "rs" is appended to the end.
#word1:  a   b 
#word2:    p   q   r   s
#merged: a p b q   r   s

#Input: word1 = "abcd", word2 = "pq"
#Output: "apbqcd"
#Explanation: Notice that as word1 is longer, "cd" is appended to the end.
#word1:  a   b   c   d
#word2:    p   q 
#merged: a p b q c   d


 def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0 #initialize 2 pointers at 0
        merged = "" #resultant string

        while i < len(word1) and j<len(word2):
            merged += word1[i] 
            i += 1 #counter for next element

            if j < len(word2):
                merged += word2[j]
                j += 1 #counter for next element
        
        merged += word1[i:] # append remaining elements if left
        merged += word2[j:]

        return merged
      
      
   
