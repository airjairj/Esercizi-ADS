#region INFO

### TRACCIA:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

### LINK: 
# https://leetcode.com/problems/two-sum/description/

### RISULTATI:

# Runtime 38ms
# Beats 78.02% of users with Python

# Memory 14.14MB
# Beats 50.21% of users with Python

#endregion

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        dic[nums[0]] = 0

        for i in range(1, len(nums)):
            attuale = target - nums[i]
            if attuale in dic:
                return [i, dic[attuale]]
                       
                    
            dic[nums[i]] = i