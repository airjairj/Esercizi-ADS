#region INFO

### TRACCIA:
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

### LINK: 
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

### RISULTATI:

# Runtime 28ms
# Beats 97.74% of users with Python

# Memory 15.70MB
# Beats 98.87% of users with Python

#endregion

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not len(nums):
            return None
            
        root = self.constructTree(nums, 0, len(nums) - 1)
        return root

    def constructTree(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        node = TreeNode(nums[mid])

        node.left = self.constructTree(nums, left, mid - 1)
        node.right = self.constructTree(nums, mid + 1, right)

        return node