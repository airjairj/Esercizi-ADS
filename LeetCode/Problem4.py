#region INFO

### TRACCIA:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

### LINK: 
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

### RISULTATI:

# Runtime 114ms
# Beats 5.27% of users with Python

# Memory 13.1MB
# Beats 99.70% of users with Python

#endregion

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        if len(nums1) == 0 or len(nums2) == 0:
            if len(nums1) == 0:
                if len(nums2) % 2 == 0:
                    centro = (len(nums2)) // 2
                    return ((nums2[centro]+nums2[centro-1])/2.0)
                else:
                    centro = (len(nums2)) // 2
                    return ((nums2[centro]))
            else:
                if len(nums1) % 2 == 0:
                    centro = (len(nums1)) // 2
                    return ((nums1[centro]+nums1[centro-1])/2.0)
                else:
                    centro = (len(nums1)) // 2
                    return ((nums1[centro]))

        self.mergeSplit(nums3, 0, len(nums3)-1)

        if len(nums3) % 2 == 0:
            centro = (len(nums3)) // 2
            return ((nums3[centro]+nums3[centro-1])/2.0)
        else:
            centro = (len(nums3)) // 2
            return ((nums3[centro]))

    def mergeSplit(self, seq, sinistra, destra):

        if sinistra < destra:
            # Trovo il centro con la divisione intera ( // ) 
            centro = (sinistra + destra) // 2

            # Ricorsione da sinistra al centro e da centro+1 a destra
            self.mergeSplit(seq, sinistra, centro)
            self.mergeSplit(seq, centro + 1, destra)

            # Avvio il sort
            self.mergeSort(seq, sinistra, centro, destra)

    def mergeSort(self, seq, sinistra, centro, destra):
        conteggio_scambi = 0

        lunghezza_sinistra = centro - sinistra + 1
        lunghezza_destra = destra - centro

        lista_sinistra = seq[sinistra:centro + 1]
        lista_destra = seq[centro + 1:destra + 1]

        # Contatori
        i, j, k = 0, 0, sinistra

        while i < lunghezza_sinistra and j < lunghezza_destra:

            if lista_sinistra[i] <= lista_destra[j]:
                seq[k] = lista_sinistra[i]
                i += 1

            else:
                seq[k] = lista_destra[j]
                j += 1
            k += 1

        while i < lunghezza_sinistra:
            seq[k] = lista_sinistra[i]
            i += 1
            k += 1

        while j < lunghezza_destra:
            seq[k] = lista_destra[j]
            j += 1
            k += 1

        return seq