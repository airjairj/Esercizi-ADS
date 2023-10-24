#region INFO

### TRACCIA:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

### LINK: 
# https://leetcode.com/problems/longest-common-prefix/description/

### RISULTATI:

# Runtime 14ms
#Beats 80.65% of users with Python

# Memory 13.43MB
#Beats 62.79% of users with Python

#endregion

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type lista: List[str]
        :rtype: str
        """

        if len(strs) == 1:
            return strs[0]

        return self.split(strs, 0, len(strs)-1)

    def cerca(self, sinistra, destra):
        min_len = min(len(sinistra), len(destra))
        for i in range(min_len):
            if sinistra[i] != destra[i]:
                return sinistra[:i]
        return sinistra[:min_len]

    def split(self, lista, sinistra, destra):
        if sinistra == destra:
            return lista[sinistra]

        centro = (sinistra + destra) // 2

        prefisso_sin = self.split(lista, sinistra, centro)
        prefisso_des = self.split(lista, centro + 1, destra)

        return self.cerca(prefisso_sin, prefisso_des)
