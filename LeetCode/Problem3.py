#region INFO

### TRACCIA:
# Given a string s, find the length of the longest substring without repeating characters.

### LINK: 
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

### RISULTATI:

# Runtime 25ms
# Beats 93.37% of users with Python

# Memory 13.50MB
# Beats 79.13% of users with Python

#endregion

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_finale = ""
        s_attuale = ""

        if not s:
            return 0

        for char in s:
            if char in s_attuale:
                index = s_attuale.index(char)
                s_attuale = s_attuale[index + 1:] + char

            else:
                s_attuale += char

                if len(s_attuale) > len(s_finale):
                    s_finale = s_attuale


        print(s_finale)
        return len(s_finale) 