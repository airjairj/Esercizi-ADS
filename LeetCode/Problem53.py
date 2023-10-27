#region INFO

### TRACCIA:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

### LINK: 
# https://leetcode.com/problems/maximum-subarray/description/

### RISULTATI:

# Runtime 498ms
# Beats 97.01% of users with Python

# Memory 26.18MB
# Beats 68.76% of users with Python

#endregion

class Solution(object):
    def maxSubArray(self, lista):
        """
        :type lista: List[int]
        :rtype: int
        """
        temp = 0
        tot = float('-inf')
 
        for val in lista:
            temp += val
            
            if temp > tot:
                tot = temp
            
            if temp < 0:
                temp = 0

        return tot