class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0

        a = 0
        b = 0
        dup = set()

        while b < len(s):
            if (s[b] in dup):
                m = max(m, b-a)
                dup.remove(s[a])
                a += 1
            else:
                dup.add(s[b])
                b += 1
                if (b == len(s)):
                    m = max(m, b-a)

        return m

        

