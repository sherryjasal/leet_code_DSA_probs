## Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input: strs = ["eat","tea","tan","ate","nat","bat"]
## Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Input: strs = [""]
## Output: [[""]]


## Input: strs = ["a"]
## Output: [["a"]]



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for char in range(len(strs)):
            word = ''.join(sorted(strs[char])) #make words 
            if word not in d:
                d[word] = [strs[char]]
            else:
                d[word].append(strs[char])
        
        return d.values()
        
        
## lessons learnt:
## make dictionary
## looping character through string
## make word be joining sorted strings of characters
## if dictionary of word exist then append string of characters
## else assign dictionary of word to string of characters (if word is not in dictionary)
## return dictinary values
