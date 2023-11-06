#region INFO

### TRACCIA:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

### LINK: 
# https://leetcode.com/problems/combination-sum/description/

### RISULTATI:

# Runtime 29ms
# Beats 88.44% of users with Python

# Memory 13.42MB
# Beats 16.81% of users with Python

#endregion

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(lista, start, target, attuale):
            if target == 0:
                tot.append(attuale[:])
                return

            for i in range(start, len(lista)):
                if target - lista[i] >= 0:
                    attuale.append(lista[i])
                    backtrack(lista, i, target - lista[i], attuale)
                    attuale.pop()

        tot = []
        backtrack(candidates, 0, target, [])
        return tot
