#region INFO

### TRACCIA:
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
# This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
# Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

### LINK: 
# https://leetcode.com/problems/string-to-integer-atoi/description/

### RISULTATI:

# Runtime 11ms
# Beats 94.02% of users with Python

# Memory 13.63MB
# Beats 5.22% of users with Python

#endregion

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        s_nuova = ""
        is_negativo = False
        # TAGLIAMO SPAZI
        for char in s:
            if s[0] == ' ':
                s = s[1:]
        # CONTROLLO EXTRA
            if s == "":
                return 0
        # CONTROLLO SEGNO
        if s[0] == '-':
            is_negativo = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        # CONTROLLO CIFRE
        for char in s:
            if char.isdigit():
                s_nuova += char
            else:
                break
        print(s_nuova)
        # CONVERTO IN INT
        if s_nuova != "":
            s_nuova = int(s_nuova)
        else:
            s_nuova = 0
        # CAMBIO SEGNO
        if is_negativo:
            s_nuova = s_nuova * (-1)
        # CONTROLLO OVERFLOW
        if s_nuova >= (pow(2,31)-1):
            s_nuova = (pow(2,31)-1)
        if s_nuova <= -1*pow(2,31):
            s_nuova = -1*pow(2,31)
        # RITORNO
        return s_nuova
            