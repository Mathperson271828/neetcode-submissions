class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1

        m = 0
        while a < b:
            m = max((b-a) * min(heights[a], heights[b]), m)
            if (heights[a] == heights[b]):
                a += 1
                b -= 1
            elif (heights[a] < heights[b]):
                a += 1
            else:
                b -= 1

        return m