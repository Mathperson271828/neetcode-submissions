class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a = 0
        m = 1001
        ans = ""

        t_count = {}
        t_matched = {}

        for char in t:
            if (char not in t_count):
                t_count[char] = 1
            else:
                t_count[char] += 1
        
        curr_count = {}
        for b in range(len(s)):
            if (s[b] in t_count):
                if (s[b] not in curr_count):
                    curr_count[s[b]] = 1
                else:
                    curr_count[s[b]] += 1

                if (curr_count[s[b]] == t_count[s[b]]):
                    t_matched[s[b]] = True
    
                while (curr_count[s[a]] > t_count[s[a]]):
                    curr_count[s[a]] -= 1
                    a += 1

                    while (s[a] not in t_count):
                        a += 1
                    
                
                if (sum(1 for value in t_matched.values() if value == True)
                    == len(t_count)):
                    if (b-a+1 < m):
                        m = b-a+1
                        if (b+1 < len(s)): 
                            ans = s[a:b+1]
                        else:
                            ans = s[a:]
            

            else:
                if (s[a] not in t_count):
                    a += 1
        
        return ans
