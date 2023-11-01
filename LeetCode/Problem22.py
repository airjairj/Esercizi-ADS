#region INFO

### TRACCIA:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### LINK: 
# https://leetcode.com/problems/generate-parentheses/description/

### RISULTATI:

# Runtime 7ms
# Beats 99.54% of users with Python

# Memory 13.44MB
# Beats 62.68% of users with Python

#endregion

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def backtrack(attuale, aperte, chiuse):
            if len(attuale) == 2 * n:
                totale.append(attuale)
                return

            if aperte < n:
                backtrack(attuale + '(', aperte + 1, chiuse)
            if chiuse < aperte:
                backtrack(attuale + ')', aperte, chiuse + 1)

        totale = []
        backtrack("", 0, 0)
        return totale
