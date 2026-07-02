class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0 
        res = 0
        count = {}

        for b in range(len(s)):
            if (s[b] in count):
                count[s[b]] += 1
            else:
                count[s[b]] = 1
            if (k + count[max(count, key = count.get)] >= b-a+1):
                res = max(res, b-a+1)
            else:
                count[s[a]] -= 1                   
                a += 1

        return res
