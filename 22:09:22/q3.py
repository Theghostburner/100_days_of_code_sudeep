# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastFoundIndex = 0
        count = 0
        for i in range(len(s)):
            for j in range(lastFoundIndex,len(t)):
                if(s[i] == t[j]):
                    lastFoundIndex = j+1
                    count+=1
                    break
                elif(j == len(t)-1):
                    return False
        if(count == len(s)):
            return True
        else:
            return False
                    
            
            
        