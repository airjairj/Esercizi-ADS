#region INFO

### TRACCIA:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

### LINK: 
# https://leetcode.com/problems/valid-parentheses/description/

### RISULTATI:

# Runtime 12ms
# Beats 77.22% of users with Python

# Memory 13.26MB
# Beats 84.03% of users with Python

#endregion

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" and len(stack) > 0:
                char2 = stack.pop()
                if(char2 != "("):
                    return False
            elif char == "]"and len(stack) > 0:
                char2 = stack.pop()
                if(char2 != "["):
                    return False
            elif char == "}" and len(stack) > 0:
                char2 = stack.pop()
                if(char2 != "{"):
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False