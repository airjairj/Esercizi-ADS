#region INFO

### TRACCIA:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

### LINK: 
# https://leetcode.com/problems/3sum/description/

### RISULTATI:

# Runtime 856ms
# Beats 60.33% of users with Python

# Memory 16.70MB
# Beats 50.30% of users with Python

#endregion

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        risultato = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Salto i duplicati

            sinistra, destra = i + 1, len(nums) - 1

            while sinistra < destra:
                total = nums[i] + nums[sinistra] + nums[destra]

                if total < 0:
                    sinistra += 1
                elif total > 0:
                    destra -= 1
                else:
                    risultato.append([nums[i], nums[sinistra], nums[destra]])

                    while sinistra < destra and nums[sinistra] == nums[sinistra + 1]:
                        sinistra += 1  # Salto i duplicati
                    while sinistra < destra and nums[destra] == nums[destra - 1]:
                        destra -= 1  # Salto i duplicati

                    sinistra += 1
                    destra -= 1

        return risultato
