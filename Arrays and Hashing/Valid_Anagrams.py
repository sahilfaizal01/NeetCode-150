class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def returnHashMap(string):
            hashMap = {}
            for char in string:
                if char in hashMap:
                    hashMap[char] += 1
                else:
                    hashMap[char] = 1
            return hashMap
        
        if len(s) != len(t):
            return False

        # for i in range(len(s)):
        #   s_hashMap[s[i]] = 1 + s_hashMap.get(s[i],0)
        #   t_hashMap[t[i]] = 1 + t_hashMap.get(t[i],0)

        s_hashMap = returnHashMap(s)
        t_hashMap = returnHashMap(t)

        for c in s:
            if s_hashMap[c] != t_hashMap.get(c,0): # to avoid key error
                return False
        
        return True
