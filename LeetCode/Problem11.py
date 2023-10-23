#region INFO

### TRACCIA:
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

### LINK: 
# https://leetcode.com/problems/container-with-most-water/description/

### RISULTATI:

# Runtime 524ms
# Beats 61.54% of users with Python

# Memory 23.70MB
# Beats 82.45% of users with Python

#endregion

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area_max = 0    
        
        while left < right:
            width = right - left
            
            altezza = min(height[left], height[right])
            
            area = width * altezza
            
            area_max = max(area_max, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area_max