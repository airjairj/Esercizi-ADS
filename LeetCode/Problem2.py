#region INFO

### TRACCIA:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### LINK: 
# https://leetcode.com/problems/add-two-numbers/description/

### RISULTATI:

# Runtime 42ms
# Beats 70.56% of users with Python

# Memory 13.17MB
# Beats 93.30% of users with Python

#endregion

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1 = ""
        v2 = ""

        while l1 is not None:
            v1 = v1 + str(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            v2 = v2 + str(l2.val)
            l2 = l2.next
        
        if v1:
            num1 = int(v1[::-1])
        else:
            num1 = 0
        
        if v2:
            num2 = int(v2[::-1])
        else:
            num2 = 0

        num3 = num1+num2
        v3 = str(num3)[::-1]
        lista_valori = [int(char) for char in v3]
        return self.creaLista(lista_valori, 0, len(lista_valori)-1)

    def creaLista(self, lista, indice, indiceMax):
        if indice < indiceMax:
            return ListNode(lista[indice], self.creaLista(lista, indice+1, indiceMax))
        else:
            return ListNode(lista[indice], None)