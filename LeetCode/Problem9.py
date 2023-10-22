#region INFO

### TRACCIA:
# Given an integer x, return true if x is a palindrome, and false otherwise.

### LINK: 
# https://leetcode.com/problems/palindrome-number/description/

### RISULTATI:

# Runtime  28ms
# Beats 92.57% of users with Python

# Memory 13.1MB
# Beats 68.14% of users with Python

#endregion

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        '''if x == x[::-1]:
            return True
        else:
            return False'''
        for idx, char in enumerate(x):
            if char == x[len(x)-1-idx]:
                if(idx==len(x)//2):
                    return True
            else:
                return False
            