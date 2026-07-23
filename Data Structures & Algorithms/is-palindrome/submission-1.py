class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.split(' ')
        t = []
        for i in st:
            for j in i:
                if j.isalnum():
                    t.append(j.lower())
        return t == t[::-1]
        