class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_count = {}

        for i in s:
            char_count[i] = char_count.get(i, 0) + 1

        for j in t:
            char_count[j] = char_count.get(j, 0) - 1

        for value in char_count.values():
            if value  != 0:
                return False
        return True 
        