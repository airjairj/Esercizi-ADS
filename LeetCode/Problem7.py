#region INFO

### TRACCIA:
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### LINK: 
# https://leetcode.com/problems/reverse-integer/description/

### RISULTATI:

# Runtime 11ms
# Beats 90.14% of users with Python

# Memory 13.26MB
# Beats 34.76% of users with Python

#endregion

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stringa = str(x)
        if x<0:
            stringa = stringa [1:]
        stringa = stringa[::-1]

        x_rev = int(stringa)
        if x_rev >= pow(2,31):
            return 0
        if x<0:
            x_rev = x_rev*(-1)
        
        
        return x_rev
