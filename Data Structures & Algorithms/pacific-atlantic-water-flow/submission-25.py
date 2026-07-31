class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        intersection = []
        used1 = []
        used2 = []
        seen1 = {}
        seen2 = {}

        def flow1(r, c) -> bool:
            if (r-1 == -1 or c-1 == -1):
                return True
            else:
                x1 = (heights[r+1][c] <= heights[r][c] if r < len(heights)-1 else False)
                x2 = (heights[r-1][c] <= heights[r][c] if r > 0 else False)
                x3 = (heights[r][c+1] <= heights[r][c] if c < len(heights[0])-1 else False)
                x4 = (heights[r][c-1] <= heights[r][c] if c > 0 else False)

                if ((r, c) not in used1 and (r, c) not in seen1):
                    used1.append((r, c))
                    return (x1 and flow1(r+1, c)) or (x2 and flow1(r-1, c)) or (x3 and flow1(r, c+1)) or (x4 and flow1(r, c-1))
                elif ((r, c) not in used1 and (r, c) in seen1):
                    return seen1[(r, c)]

        def flow2(r, c) -> bool:
            if (r+1 == len(heights) or c+1 == len(heights[0])):
                return True
            else:
                x1 = (heights[r+1][c] <= heights[r][c] if r < len(heights)-1 else False)
                x2 = (heights[r-1][c] <= heights[r][c] if r > 0 else False)
                x3 = (heights[r][c+1] <= heights[r][c] if c < len(heights[0])-1 else False)
                x4 = (heights[r][c-1] <= heights[r][c] if c > 0 else False)

                if ((r, c) not in used2 and (r, c) not in seen2):
                    used2.append((r, c))
                    return (x1 and flow2(r+1, c)) or (x2 and flow2(r-1, c)) or (x3 and flow2(r, c+1)) or (x4 and flow2(r, c-1))
                elif ((r, c) not in used2 and (r, c) in seen2):
                    return seen2[(r, c)]
        
        for i, row in enumerate(heights):
            for j, h in enumerate(row):
                val1 = False
                val2 = False
                if (i, j) not in seen1:
                    val1 = flow1(i, j)
                    seen1[(i, j)] = val1
                else:
                    val1 = seen1[(i, j)]
                if (i, j) not in seen2:
                    val2 = flow2(i, j)
                    seen2[(i, j)] = val2
                else:
                    val2 = seen2[(i, j)]

                if val1 and val2:
                    intersection.append((i, j))
                used1.clear()
                used2.clear()

        return intersection