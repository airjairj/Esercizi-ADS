#region INFO

### TRACCIA:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.

### LINK: 
# https://leetcode.com/problems/4sum/description/

### RISULTATI:

# Time limit exceeded (MA FUNZIONA)

#endregion

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(nums,start,target,result_temp,result):

            if target == 0 and len(result_temp) == 4:
                result.append(result_temp[:])
                return
            for i in range(start, len(nums)):
                if len(result_temp) < 4:
                    
                    result_temp.append(nums[i])
                    backtrack(nums,i + 1, target - nums[i], result_temp,result)
                    result_temp.pop() 

        self.result = []
        backtrack(nums,0, target, [],self.result)
        
        self.output = []

        for item in self.result:
            item.sort()
            if item not in self.output:
                self.output.append(item)

        return self.output