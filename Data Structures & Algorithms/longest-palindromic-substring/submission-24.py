class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        pal = {}
        def isPal(i, j):
            if (i, j) not in pal:
                if (i == j):
                    pal[(i, j)] = True
                elif (i+1 == j):
                    pal[(i, j)] = (s[i] == s[j])
                else:
                    pal[(i, j)] = (s[i] == s[j]) and isPal(i+1, j-1) 
            
            return pal[(i, j)]


        max_len = 0
        start = -1
        end = -1
        for i in range(n):
            for j in range(n):
                if i <= j:
                    if isPal(i, j) and j-i+1 > max_len:
                        start = i
                        end = j
                        max_len = j-i+1
        
        return s[start:end+1]
