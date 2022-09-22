# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution:
    def reverseWords(self, s: str) -> str:
        sentence=""
        word = ""
        for i in range(len(s)):
            if(s[i] != " "):
                word+=s[i]
                if(i == len(s) - 1):
                    reverse = word[::-1]
                    sentence+=reverse
            else:
                reverse = word[::-1]
                sentence+=reverse
                sentence+=(" ")
                word = ""
        return sentence