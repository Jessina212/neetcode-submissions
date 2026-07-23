class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for i in s:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        
        d2 = {}
        for i in t:
            if i in d2.keys():
                d2[i] += 1
            else:
                d2[i] = 1

        count = 0

        if set(s) == set(t):
            for k in d1:
                if d1[k] == d2[k]:
                    count += 1

            if count == len(set(t)):
                return True
            else:
                return False
        else: 
            return False
        


