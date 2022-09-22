# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst = {}
        mapts = {}
        for i in range(len(s)):
            if(s[i] in mapst) and (t[i] in mapts):
                if(mapst[s[i]] == t[i]) and (mapts[t[i]] == s[i]):
                    continue
                else:
                    return False
                
            elif(s[i] not in mapst) and (t[i] not in mapts):
                mapst[s[i]] = t[i]
                mapts[t[i]] = s[i]
            else:
                return False
        return True
                