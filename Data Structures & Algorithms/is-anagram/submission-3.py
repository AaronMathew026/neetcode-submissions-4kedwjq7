class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in t_list:
                return False
            t_list.remove(letter)
        return True