class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        found = set()
        islands = 0

        def search(self, x: int, y: int):
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in found:
                found.add((x, y))
                search(self, x-1, y)
                search(self, x+1, y)
                search(self, x, y-1)
                search(self, x, y+1)

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "1" and (i, j) not in found:
                    search(self, i, j)
                    islands += 1
            
        return islands