#region INFO

### TRACCIA:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

### LINK: 
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

### RISULTATI:

# Runtime 10ms
# Beats 93.07% of users with Python

# 13.26MB
# Beats 37.59% of users with Python

#endregion

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        primavolta = True
        testa = head
        nodo = None
        m = 0
        mm = 0
        k = 1
        precedente = None
        while k != None:
            if m == mm:
                k = head.next
            else:
                k = k.next # type: ignore

            m+=1

        print(m)
        while m-n > 0:
            if primavolta:
                nodo = head
                primavolta = False
                precedente = None
            else:
                precedente = nodo

                if nodo and nodo.next:
                    nodo = nodo.next 
                else:
                    nodo = None

                m-=1

        if precedente and primavolta == False:
            if nodo and nodo.next:
                precedente.next = nodo.next
            else:
                precedente.next = None
        elif primavolta == False:
            return None
        else:
            return head.next

        return testa