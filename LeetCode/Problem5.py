#region INFO

### TRACCIA:
# Given a string s, return the longest palindromic substring in s.

### LINK: 
# https://leetcode.com/problems/longest-palindromic-substring/description/

### RISULTATI:

# Runtime 340ms
# Beats 86.39% of users with Python

# Memory 13.20MB
# Beats 97.81% of users with Python

#endregion

class Solution:
    def longestPalindrome(self, s):
        risposta = ''

        if len(s) == 1:
            return s

        for centro in range(len(s)):
            palindromo1 = espandi(s, centro, centro) # dispari
            palindromo2 = espandi(s, centro, centro + 1) # pari
            risposta = max(risposta, palindromo1, palindromo2, key=len)
        return risposta

def espandi(s, sinistra, destra):
    while sinistra >= 0 and destra < len(s) and s[sinistra] == s[destra]:
        sinistra -= 1
        destra += 1
    return s[sinistra + 1:destra]
