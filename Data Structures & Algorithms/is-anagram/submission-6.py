class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # check len of s and t
        if len(s) != len(t):
            return False
        
        # traverse each s and t
        s_hmap = { c: 0 for c in s }
        t_hmap = { c: 0 for c in t }

        # find frequency of each
        for i in range(len(s)):
            s_hmap[s[i]] += 1
            t_hmap[t[i]] += 1
        
        return s_hmap == t_hmap

        
        