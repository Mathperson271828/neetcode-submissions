class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbor = {i:[] for i in range(n)}

        for edge in edges:
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])
    
        visited = set()

        def dfs(val: int):
            visited.add(val)

            for node in neighbor[val]:
                if node not in visited:
                    dfs(node)

        com = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                com += 1

        return com