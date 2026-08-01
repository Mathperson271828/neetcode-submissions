class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = {i: [] for i in range(numCourses)}
        for row in prerequisites:
            neighbors[row[1]].append(row[0])
        
        state = [0] * numCourses
        
        def dfs(course: int) -> bool:
            if (state[course] == 1):
                return False
            elif (state[course] == 2):
                return True

            state[course] = 1
            for neighbor in neighbors[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True