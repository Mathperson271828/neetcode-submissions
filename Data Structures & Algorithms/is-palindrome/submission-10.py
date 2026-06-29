import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        size = len(s)

        a = 0
        b = size-1
        isTrue = True

        while a < b:
            if (s[a] != s[b]):
                isTrue = False
                break
            else:
                a = a+1
                b = b-1
        
        return isTrue