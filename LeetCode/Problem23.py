#region INFO

### TRACCIA:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

### LINK: 
# https://leetcode.com/problems/merge-k-sorted-lists/description/

### RISULTATI:

# Runtime 71ms
#Beats 73.98% of users with Python

# Memory 19.11MB
# Beats 94.72% of users with Python

#endregion

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next       
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        
        return dummy.next