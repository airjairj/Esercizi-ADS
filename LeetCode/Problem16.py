#region INFO

### TRACCIA:
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

### LINK: 
# https://leetcode.com/problems/3sum-closest/description/

### RISULTATI:

# Runtime 432ms
# Beats 84.76% of users with Python

# Memory 13.10MB
# Beats 98.42% of users with Python

#endregion

class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def threeSumClosest(self, nums, target):
        nums.sort()
        risultato = float('inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            sinistra, destra = i + 1, len(nums) - 1

            while sinistra < destra:
                total = nums[i] + nums[sinistra] + nums[destra]

                if total < target:
                    sinistra += 1
                    if target - total < abs(risultato - target):
                        risultato = total
                elif total > target:
                    destra -= 1
                    if total - target < abs(risultato - target):
                        risultato = total
                else:
                    return total


        return risultato
