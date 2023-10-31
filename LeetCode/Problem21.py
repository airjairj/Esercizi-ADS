#region INFO

### TRACCIA:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

### LINK: 
# https://leetcode.com/problems/merge-two-sorted-lists/description/

### RISULTATI:

# Runtime 15ms
# Beats 85.00% of users with Python

# 13.27MB
# Beats 57.87% of users with Python

#endregion

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def merge(nodo1, nodo2):
            if not nodo1:
                return nodo2
            if not nodo2:
                return nodo1

            if nodo1.val <= nodo2.val:
                merged = nodo1
                merged.next = merge(nodo1.next, nodo2)
            else:
                merged = nodo2
                merged.next = merge(nodo1, nodo2.next)
            return merged

        return merge(list1, list2)