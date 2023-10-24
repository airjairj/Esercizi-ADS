#region INFO

### TRACCIA:
# Given an integer, convert it to a roman numeral.

### LINK: 
# https://leetcode.com/problems/integer-to-roman/description/

### RISULTATI:

# Runtime 23ms
# Beats 87.11% of users with Python

# Memory 13.12MB
# Beats 68.33% of users with Python

#endregion

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #migliaia = num/1000
        #centinaia = (num%1000)/100
        #decine = (num%100) /10
        #uni = num%10

        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        D = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        U = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return M[num/1000] + C[(num%1000)/100] + D[(num%100) /10] + U[num%10]