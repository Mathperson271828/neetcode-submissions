class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {i:[] for i in range(n)}
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        state = [0] * n

        def dfs(val: int, prev: int) -> bool:
            if (state[val] == 1):
                return False
            elif (state[val] == 2):
                return True

            state[val] = 1
            for node in neighbors[val]:
                if not dfs(node, val) and node != prev:
                    return False
            state[val] = 2
            return True
        
        for i in range(n):
            if not dfs(i, i):
                return False
        if len(edges) == n-1:
            return True
        else:
            return False
         
            